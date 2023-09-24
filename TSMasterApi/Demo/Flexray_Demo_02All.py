from TSMasterAPI import *
def crc8(data, dataId):
    data2 = [dataId & 0x00FF,(dataId & 0xFF00) >> 8] + data
    Rtn = 00^0X00
    for i in range(len(data2)):
        Rtn = (Rtn ^ data2[i])&0xff
        for j in range(8):
            if (Rtn & 0x80):
                Rtn = ((Rtn << 1) ^ 0x1D)&0xff
            else:
                Rtn = (Rtn << 1)&0xff
    return Rtn
def get_definition(ASignalAddress:bytes):
    ASignalDef=TFlexRaySignal()
    ret = tscom_flexray_get_signal_definition(ASignalAddress,ASignalDef)
    if ret == 0:
        return ASignalDef
    return None
class USGMode(IntEnum):
    UsgModAbdnd=0
    UsgModInActv=1
    UsgModCnvinc=2
    UsgModActv=11
    UsgModDrvg=13

class TOSUN():
    def __init__(self,APPName:c_char_p) -> None:
        self.APPName = APPName
        initialize_lib_tsmaster(self.APPName)
        tsapp_set_can_channel_count(0)
        tsapp_set_lin_channel_count(0)
        tsapp_set_flexray_channel_count(2)
        tsapp_set_mapping_verbose(self.APPName,TLIBApplicationChannelType.APP_FlexRay,CHANNEL_INDEX.CHN1,b"TC1034",TLIBBusToolDeviceType.TS_USB_DEVICE,TLIB_TS_Device_Sub_Type.TC1034,0,CHANNEL_INDEX.CHN1,True)
        tsapp_set_mapping_verbose(self.APPName,TLIBApplicationChannelType.APP_FlexRay,CHANNEL_INDEX.CHN2,b"TC1034",TLIBBusToolDeviceType.TS_USB_DEVICE,TLIB_TS_Device_Sub_Type.TC1034,0,CHANNEL_INDEX.CHN2,True)
        self.onrxtxevnet = OnTx_RxFUNC_Flexray(self.on_tx_rx)
        self.onpretxevnet = OnTx_RxFUNC_Flexray(self.on_pre_tx)
        self.MsgList = []
        self.obj = s32(0)
    def __unloadDBS(self):
        tsdb_unload_flexray_dbs()
    def __loadDB(self,dbpath:str):
        self.AdbID = s32(0)
        self.dbinfo = Fibex_parse(dbpath)
        tsdb_load_flexray_db(dbpath.encode("utf8"),b"0,1",self.AdbID)
        self.get_signals_definition()
    def connect(self,dbpath:str):
        self.__unloadDBS()
        self.__loadDB(dbpath)
        tsapp_register_event_flexray(self.obj ,self.onrxtxevnet)
        tsapp_register_pretx_event_flexray(self.obj ,self.onpretxevnet)
        tsapp_connect()
        FlexrayConfig = TLibFlexray_controller_config().set_controller_config(self.dbinfo.Ecus['VDDM'],is_open_a=True, is_open_b=False, enable100_b=True, is_show_nullframe=False,is_Bridging=True)
        self.CHN0Frames = []
        # 按照工程配置，发送的报文 为VDDM CEM两节点下所有发送报文
        for frame in self.dbinfo.Ecus['VDDM']['TX_Frame']:
            self.CHN0Frames.append(frame)
        for frame in self.dbinfo.Ecus['CEM']['TX_Frame']:
            self.CHN0Frames.append(frame)
        # 对 发送报文进行排序
        self.CHN0Frames.sort(key=lambda k: (k.get('SLOT-ID', 0)))
        fr_trigger_len = len(self.CHN0Frames)
        fr_trigger = (TLibTrigger_def * fr_trigger_len)()
        FrameLengthArray = (c_int * fr_trigger_len)()
        for idx in range(fr_trigger_len):
            FrameLengthArray[idx] = self.CHN0Frames[idx]['FDLC']
            fr_trigger[idx].frame_idx=idx
            fr_trigger[idx].slot_id = self.CHN0Frames[idx]['SLOT-ID']
            fr_trigger[idx].cycle_code = self.CHN0Frames[idx]['BASE-CYCLE']+self.CHN0Frames[idx]['CYCLE-REPETITION']
            if fr_trigger[idx].slot_id == fr_trigger[0].slot_id:
                fr_trigger[idx].config_byte = 0X31
            elif fr_trigger[idx].slot_id > self.dbinfo.STATIC_SLOT:
                fr_trigger[idx].config_byte = 0xA9
            else:
                fr_trigger[idx].config_byte = 0X01
        tsflexray_set_controller_frametrigger(0, FlexrayConfig, FrameLengthArray, fr_trigger_len, fr_trigger, fr_trigger_len, 1000)

        FlexrayConfig1 = TLibFlexray_controller_config().set_controller_config(self.dbinfo.Ecus['VGM'],is_open_a=True, is_open_b=True, enable100_b=True, is_show_nullframe=False,is_Bridging=True)
        self.CHN1Frames = []

        # 按照工程配置，发送的报文 为VDDM CEM两节点下所有发送报文
        for frame in self.dbinfo.Ecus['VGM']['TX_Frame']:
            self.CHN1Frames.append(frame)
        self.CHN1Frames.sort(key=lambda k: (k.get('SLOT-ID', 0)))
        fr_trigger_len1 = len(self.CHN1Frames)
        fr_trigger1 = (TLibTrigger_def * fr_trigger_len1)()
        FrameLengthArray1 = (c_int * fr_trigger_len1)()
        for idx in range(fr_trigger_len1):
            FrameLengthArray1[idx] = self.CHN1Frames[idx]['FDLC']
            fr_trigger1[idx].frame_idx=idx
            fr_trigger1[idx].slot_id = self.CHN1Frames[idx]['SLOT-ID']
            fr_trigger1[idx].cycle_code = self.CHN1Frames[idx]['BASE-CYCLE']+self.CHN1Frames[idx]['CYCLE-REPETITION']
            if fr_trigger1[idx].slot_id == fr_trigger1[0].slot_id:
                fr_trigger1[idx].config_byte = 0X31
            elif fr_trigger1[idx].slot_id > self.dbinfo.STATIC_SLOT:
                fr_trigger1[idx].config_byte = 0xA9
            else:
                fr_trigger1[idx].config_byte = 0X01
        tsflexray_set_controller_frametrigger(1, FlexrayConfig1, FrameLengthArray1, fr_trigger_len1, fr_trigger1, fr_trigger_len1, 1000)
        tscom_flexray_rbs_activate_cluster_by_name(0,True,b'BackboneFR',False)
        tscom_flexray_rbs_activate_ecu_by_name(0,True,b"BackboneFR",b"VDDM",True)
        tscom_flexray_rbs_activate_ecu_by_name(0,True,b"BackboneFR",b"CEM",True)

        tscom_flexray_rbs_activate_cluster_by_name(1,True,b'BackboneFR',False)
        tscom_flexray_rbs_activate_ecu_by_name(1,True,b"BackboneFR",b"VGM",True)

        tscom_flexray_rbs_configure(False,True,True,2)
        tscom_flexray_rbs_enable(True)
        tscom_flexray_rbs_start()
        self.start()
        self.__send_initMsg()
    def __send_initMsg(self):
        AFlexray = TLIBFlexray(0,2,1,32,4,[0XC0,0X52,0X7B,0XFF,0X97])
        tsapp_transmit_flexray_async(AFlexray)
        AFlexray1 = TLIBFlexray(0,8,1,32,4,[0XC0,0X53,0Xff,0XFF,0Xb7,0x02])
        tsapp_transmit_flexray_async(AFlexray1)
        AFlexray2 = TLIBFlexray(0,8,1,37,2,[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xB6, 0xD0, 0x00, 0x21, 0x21, 0x21, 0x36, 0x06, 0x21, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x06])
        tsapp_transmit_flexray_async(AFlexray2)
        AFlexray3 = TLIBFlexray(0,8,1,39,8,[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xD0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        tsapp_transmit_flexray_async(AFlexray3)
        tscom_flexray_rbs_set_signal_value_by_address(b"0/BackboneFR/CEM/CemBackBoneFr02/VehModMngtGlbSafe1UsgModSts",USGMode.UsgModCnvinc)

    def disconnect(self):
        tscom_flexray_rbs_enable(False)
        tscom_flexray_rbs_stop()
        self.stop()
        tsapp_disconnect()
    def start(self):
        for i in range(2):
            tsflexray_start_net(i, 1000)
    def stop(self):
        for i in range(2):
            tsflexray_stop_net(i, 1000)
    def finally_exit(self):
        finalize_lib_tsmaster()
    
    def get_signals_definition(self):
        CemBackBoneFr02 = { }
        CemBackBoneFr02['Msginfo'] = [36,0,1]
        CemBackBoneFr02['dataId'] = 116
        CemBackBoneFr02['data'] = []
        CemBackBoneFr02['signals'] = []
        CemBackBoneFr02['signals'].append({"Name":get_definition(b'0/BackboneFR/CEM/CemBackBoneFr02/VehModMngtGlbSafe1Cntr'),"value":0})
        CemBackBoneFr02['signals'].append({"Name":get_definition(b'0/BackboneFR/CEM/CemBackBoneFr02/VehModMngtGlbSafe1CarModSts1'),"value":0})
        for i in range(6):
            CemBackBoneFr02['signals'].append({"Name":None,"value":0.0})
        CemBackBoneFr02['signals'].append({"Name":get_definition(b'0/BackboneFR/CEM/CemBackBoneFr02/VehModMngtGlbSafe1UsgModSts'),"value":0})
        CemBackBoneFr02['signals'].append({"Name":get_definition(b'0/BackboneFR/CEM/CemBackBoneFr02/VehModMngtGlbSafe1Chks'),"value":0})
        CemBackBoneFr02['signals'].append({"Name":get_definition(b'0/BackboneFR/CEM/CemBackBoneFr02/VehModMngtGlbSafe1_UB'),"value":1})
        self.MsgList.append(CemBackBoneFr02)

        BcmVddmBackBoneFr06 = {}
        BcmVddmBackBoneFr06['Msginfo'] = [57,0,4]
        BcmVddmBackBoneFr06['dataId'] = 55
        BcmVddmBackBoneFr06['data'] = []
        BcmVddmBackBoneFr06['signals'] = []
        BcmVddmBackBoneFr06['signals'].append({"Name":get_definition(b'0/BackboneFR/VDDM/BcmVddmBackBoneFr06/VehSpdLgtCntr'),"value":0})
        BcmVddmBackBoneFr06['signals'].append({"Name":get_definition(b'0/BackboneFR/VDDM/BcmVddmBackBoneFr06/VehSpdLgtA'),"value":0})
        BcmVddmBackBoneFr06['signals'].append({"Name":get_definition(b'0/BackboneFR/VDDM/BcmVddmBackBoneFr06/VehSpdLgtQf'),"value":0})
        BcmVddmBackBoneFr06['signals'].append({"Name":get_definition(b'0/BackboneFR/VDDM/BcmVddmBackBoneFr06/VehSpdLgtChks'),"value":0})
        BcmVddmBackBoneFr06['signals'].append({"Name":get_definition(b'0/BackboneFR/VDDM/BcmVddmBackBoneFr06/VehSpdLgt_UB'),"value":1})
        self.MsgList.append(BcmVddmBackBoneFr06)


    def on_tx_rx(self,obj,AFlexRay):
        if AFlexRay.contents.FDir == 1:
            for index in range(len(self.MsgList)):
                if(AFlexRay.contents.FSlotId == self.MsgList[index]['Msginfo'][0] and AFlexRay.contents.FCycleNumber % self.MsgList[index]['Msginfo'][2] == self.MsgList[index]['Msginfo'][1]):
                    self.MsgList[index]['signals'][0]['value'] += 1
                    if self.MsgList[index]['signals'][0]['value']>14:
                        self.MsgList[index]['signals'][0]['value'] = 0
                    flexray_rbs_update_frame_by_header(AFlexRay)
                    return
    def on_pre_tx(self,obj,AFlexRay):
        for index in range(len(self.MsgList)):
            if(AFlexRay.contents.FSlotId == self.MsgList[index]['Msginfo'][0] and AFlexRay.contents.FCycleNumber % self.MsgList[index]['Msginfo'][2] == self.MsgList[index]['Msginfo'][1]):
                self.MsgList[index]['data'].append(int(self.MsgList[index]['signals'][0]['value'])) 
                tscom_set_flexray_signal_value(self.MsgList[index]['signals'][0]['Name'],AFlexRay.contents.FData,self.MsgList[index]['data'][0])
                for singalindex in range(1,len(self.MsgList[index]['signals'])-2):
                    if self.MsgList[index]['signals'][singalindex]['Name']!= None:
                        self.MsgList[index]['signals'][singalindex]['value']= int(get_flexray_signal_raw_value(self.MsgList[index]['signals'][singalindex]['Name'],AFlexRay.contents.FData))
                        singal_len =  int(self.MsgList[index]['signals'][singalindex]['Name'].FLength/8) + 1
                        value = int(self.MsgList[index]['signals'][singalindex]['value'])
                        for LCount_idx in range(singal_len):
                            self.MsgList[index]['data'].append((value>>(8*LCount_idx)) & 0xff)
                    else:
                        self.MsgList[index]['data'].append(int(self.MsgList[index]['signals'][singalindex]['value']))
                tscom_set_flexray_signal_value(self.MsgList[index]['signals'][-2]['Name'],AFlexRay.contents.FData,crc8(self.MsgList[index]['data'],self.MsgList[index]['dataId']))
                tscom_set_flexray_signal_value(self.MsgList[index]['signals'][-1]['Name'],AFlexRay.contents.FData,self.MsgList[index]['signals'][-1]['value'])
                self.MsgList[index]['data'].clear()
                return
    def set_usgMode(self,usgmode:USGMode):
        tscom_flexray_rbs_set_signal_value_by_address(b"0/BackboneFR/CEM/CemBackBoneFr02/VehModMngtGlbSafe1UsgModSts",usgmode)
    def set_speed(self,speed = 10):
        tscom_flexray_rbs_batch_set_start()
        tscom_flexray_rbs_batch_set_signal(b"0/BackboneFR/VDDM/BcmVddmBackBoneFr04/VehSpdLgtTar",speed)
        tscom_flexray_rbs_batch_set_signal(b"0/BackboneFR/VDDM/BcmVddmBackBoneFr04/VehSpdLgtTar_UB",1)
        tscom_flexray_rbs_batch_set_signal(b"0/BackboneFR/VDDM/BcmVddmBackBoneFr06/VehSpdLgtA",speed)
        tscom_flexray_rbs_batch_set_signal(b"0/BackboneFR/VDDM/BcmVddmBackBoneFr06/VehSpdLgtQf",3)
        tscom_flexray_rbs_batch_set_end()
    def set_gear(self,gear = 1):
        tscom_flexray_rbs_batch_set_start()
        tscom_flexray_rbs_batch_set_signal(b"0/BackboneFR/VDDM/VddmBackBoneFr03/GearLvrIndcn",gear)
        tscom_flexray_rbs_batch_set_signal(b"0/BackboneFR/VDDM/VddmBackBoneFr03/GearLvrIndcn_UB",1)
        tscom_flexray_rbs_batch_set_end()
    def set_acc_and_lcc(self,indicator=3):
        tscom_flexray_rbs_batch_set_start()
        tscom_flexray_rbs_batch_set_signal(b"0/BackboneFR/ASDM/AsdmBackBoneFr11/AsyALgtIndcr",indicator)
        tscom_flexray_rbs_batch_set_signal(b"0/BackboneFR/ASDM/AsdmBackBoneFr11/AsyALgtIndcr_UB",1)
        tscom_flexray_rbs_batch_set_signal(b"0/BackboneFR/ASDM/AsdmBackBoneFr11/AsyALatIndcr",indicator)
        tscom_flexray_rbs_batch_set_signal(b"0/BackboneFR/ASDM/AsdmBackBoneFr11/AsyALatIndcr_UB",1)
        tscom_flexray_rbs_batch_set_end()

    def in_STR_mode(self):
        print("start..sleep...")
        tscom_flexray_rbs_batch_set_start()
        tscom_flexray_rbs_batch_set_signal(b"0/BackboneFR/CEM/CemBackBoneFr03/AmbTRaw_UB",1)
        tscom_flexray_rbs_batch_set_signal(b"0/BackboneFR/CEM/CemBackBoneFr03/AmbTRawAmbTVal",20)

        tscom_flexray_rbs_batch_set_signal(b"0/BackboneFR/CEM/CemBackBoneFr02/VehModMngtGlbSafe1CarModSts1",0)
        tscom_flexray_rbs_batch_set_signal(b"0/BackboneFR/CEM/CemBackBoneFr02/VehModMngtGlbSafe1EgyLvlElecMai",0)

        tscom_flexray_rbs_batch_set_signal(b"0/BackboneFR/VDDM/VddmBackBoneFr06/DispHvBattLvlOfChrg_UB",1)
        tscom_flexray_rbs_batch_set_signal(b"0/BackboneFR/VDDM/VddmBackBoneFr06/DispHvBattLvlOfChrg",25)

        tscom_flexray_rbs_batch_set_signal(b"0/BackboneFR/VDDM/VddmBackBoneFr10/DrvPfmncRedn_UB",1)
        tscom_flexray_rbs_batch_set_signal(b"0/BackboneFR/VDDM/VddmBackBoneFr10/DrvPfmncRedn",0)  
        tscom_flexray_rbs_batch_set_end()
        tosun.set_usgMode(USGMode.UsgModCnvinc)
        time.sleep(2)
        self.set_usgMode(USGMode.UsgModInActv)
        time.sleep(2)
        tosun.set_usgMode(USGMode.UsgModAbdnd)
        time.sleep(2)
        self.stop()  # 心跳包 3 秒后停止
        time.sleep(60)  # current = 0.044A
        print("done..sleep...")
    def out_STR_mode(self):
        print("start..wakeup...")
        self.start()
        tosun.set_usgMode(USGMode.UsgModAbdnd)
        time.sleep(2)
        self.set_usgMode(USGMode.UsgModInActv)
        time.sleep(2)
        tosun.set_usgMode(USGMode.UsgModCnvinc)
        time.sleep(2)
        print("done..wakeup...")

if __name__ == '__main__':

    tosun = TOSUN(b"TSMasterFlexray")

    tosun.connect(r'C:\Users\yueto\Desktop\SDB21206_HX11_Low_BackboneFR_220513.xml')

    tosun.set_usgMode(USGMode.UsgModCnvinc)

    time.sleep(60)

    tosun.set_speed()

    tosun.set_gear()

    tosun.set_acc_and_lcc()

    tosun.set_usgMode(USGMode.UsgModDrvg)

    tosun.set_usgMode(USGMode.UsgModCnvinc)

    tosun.set_usgMode(USGMode.UsgModAbdnd)
    
    tosun.set_usgMode(USGMode.UsgModDrvg)

    tosun.set_usgMode(USGMode.UsgModCnvinc)

    time.sleep(10)

    i=1
    print(f"开始执行时间为{time.time()}")
    for i in range(2000):
        time1=time.time()
        try:
            tosun.in_STR_mode()  # 进入STR模式
            time.sleep(10)
            tosun.out_STR_mode()  # 退出STR模式
            time.sleep(10)
        except Exception as e:
            print(f"exception: {e}")
        time2 = time.time()
        time3=time2-time1
        print(f'该轮次执行时长为{time3}')
        print(f'当前执行了{i}轮')
    print(f'实际共执行了{i}轮')
    tosun.disconnect()
    tosun.finally_exit()
