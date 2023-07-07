from TSMasterAPI import *
def crc8(data, len, dataId):
    data2 = [dataId & 0x00FF,(dataId & 0xFF00) >> 8] + data
    Rtn = 00^0X00
    for i in range(len(data2)):
        Rtn = Rtn ^ data2[i]
        for j in range(8): 
            if (Rtn & 0x80):
                Rtn = (Rtn << 1) ^ 0x1D
            else:
                Rtn = Rtn << 1
    return Rtn

class TOSUN():
    def __init__(self,APPName:c_char_p) -> None:
        self.APPName = APPName
        initialize_lib_tsmaster(self.APPName)
        tsapp_set_can_channel_count(0)
        tsapp_set_lin_channel_count(0)
        tsapp_set_flexray_channel_count(2)
        tsapp_set_mapping_verbose(self.APPName,TLIBApplicationChannelType.APP_FlexRay,CHANNEL_INDEX.CHN1,b"TC1034",TLIBBusToolDeviceType.TS_USB_DEVICE,TLIB_TS_Device_Sub_Type.TC1034,0,CHANNEL_INDEX.CHN1,True)
        tsapp_set_mapping_verbose(self.APPName,TLIBApplicationChannelType.APP_FlexRay,CHANNEL_INDEX.CHN2,b"TC1034",TLIBBusToolDeviceType.TS_USB_DEVICE,TLIB_TS_Device_Sub_Type.TC1034,0,CHANNEL_INDEX.CHN2,True)
    def __unloadDBS(self):
        tsdb_unload_flexray_dbs()
    def __loadDB(self,dbpath:str):
        self.AdbID = s32(0)
        self.dbinfo = Fibex_parse(dbpath)
        tsdb_load_flexray_db(dbpath.encode("utf8"),b"0,1",self.AdbID)
    def connect(self,dbpath:str):
        self.__unloadDBS()
        self.__loadDB(dbpath)
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
        # tscom_flexray_rbs_activate_cluster_by_name(0,True,b'BackboneFR',False)
        # tscom_flexray_rbs_activate_ecu_by_name(0,True,b"BackboneFR",b"VDDM",True)
        # tscom_flexray_rbs_activate_ecu_by_name(0,True,b"BackboneFR",b"CEM",True)

        # tscom_flexray_rbs_activate_cluster_by_name(1,True,b'BackboneFR',False)
        # tscom_flexray_rbs_activate_ecu_by_name(1,True,b"BackboneFR",b"VGM",True)

        # tscom_flexray_rbs_configure(False,True,True,2)
        # tscom_flexray_rbs_enable(True)
        # tscom_flexray_rbs_start()
        self.start()
        self.__send_initMsg()
    def __send_initMsg(self):
        AFlexray = TLIBFlexray(0,2,1,32,4,[0XC0,0X52,0X7B,0XFF,0X97])
        tsapp_transmit_flexray_async(AFlexray)
        AFlexray1 = TLIBFlexray(0,8,1,32,4,[0XC0,0X53,0Xff,0XFF,0Xb7,0x02])
        tsapp_transmit_flexray_async(AFlexray1)
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
if __name__ == '__main__':

    # tosun = TOSUN(b"TSMasterFlexray")

    # tosun.connect(r'D:\IDE\libTSCANApi\DataBases\SDB21206_HX11_Low_BackboneFR_220513.xml')

    # time.sleep(10)

    # tosun.disconnect()

    # tosun.finally_exit()
    a = [1,2,4]
    b = [0,5]
    print(b+a)