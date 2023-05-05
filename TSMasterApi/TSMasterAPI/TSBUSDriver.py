'''
Author: seven 865762826@qq.com
Date: 2023-04-21 11:19:14
LastEditors: seven 865762826@qq.com
LastEditTime: 2023-04-24 10:03:01
'''
import time
from TSCommon import *


mapping = {
    "CAN":{"CHNCount":4,"HW_Names":["TC1014","TC1014","TC1014"],"HW_Chns":["0,1","0","3"]},
    "LIN":{"CHNCount":4,"HW_Names":["TC1016","TC1016","TC1016"],"HW_Chns":["0,1","0","1"]},
    "Flexray":{"CHNCount":4,"HW_Names":["TC1034","TC1034","TC1034"],"HW_Chns":["0,1","0","1"]}
}

def set_mapping(mapping):
    AppName = c_char_p()
    tsapp_get_current_application(AppName)
    if 'CAN' in mapping and "CHNCount"in mapping['CAN'] and "HW_Names"in mapping['CAN'] and "HW_Chns"in mapping['CAN']:
        tsapp_set_can_channel_count(mapping['CAN']['CHNCount'])
        HW_Names_len = len(mapping['CAN']['HW_Names'])
        HW_Chns_len = len(mapping['CAN']['HW_Chns'])
        if(HW_Names_len != HW_Chns_len):
            raise Exception("Length of HW_Names and HW_Chns must match")
        Mapping_channel_count = 0
        for i in range(HW_Chns_len):
            Mapping_channel_count += len(mapping['CAN']['HW_Chns'][i].split(','))
        if Mapping_channel_count>mapping['CAN']['CHNCount']:
            raise Exception("Number of channels in mapping is higher than number of channels on the board")
        FCount = 0
        hw = []
        for i in range(HW_Names_len):
            hw.append(mapping['CAN']['HW_Names'][i])
            hw_sub_index = hw.count(mapping['CAN']['HW_Names'][i]) - 1
            chn_str = mapping['CAN']['HW_Chns'][i].split(',')
            for chn in chn_str:
                tsapp_set_mapping_verbose(AppName,TLIBApplicationChannelType.APP_CAN,FCount,mapping['CAN']['HW_Names'][i].encode('utf8'),3,HW_dict[mapping['CAN']['HW_Names'][i]],hw_sub_index,int(chn),True)
                FCount += 1
    else:
        tsapp_set_can_channel_count(0)
    if 'LIN' in mapping and "CHNCount"in mapping['LIN'] and "HW_Names"in mapping['LIN'] and "HW_Chns"in mapping['LIN']:
        tsapp_set_lin_channel_count(mapping['LIN']['CHNCount'])
        HW_Names_len = len(mapping['LIN']['HW_Names'])
        HW_Chns_len = len(mapping['LIN']['HW_Chns'])
        if(HW_Names_len != HW_Chns_len):
            raise Exception("Length of HW_Names and HW_Chns must match")
        Mapping_channel_count = 0
        for i in range(HW_Chns_len):
            Mapping_channel_count += len(mapping['LIN']['HW_Chns'][i].split(','))
        if Mapping_channel_count>mapping['LIN']['CHNCount']:
            raise Exception("Number of channels in mapping is higher than number of channels on the board")
        FCount = 0
        hw = []
        for i in range(HW_Names_len):
            hw.append(mapping['LIN']['HW_Names'][i])
            hw_sub_index = hw.count(mapping['LIN']['HW_Names'][i]) - 1
            chn_str = mapping['LIN']['HW_Chns'][i].split(',')
            for chn in chn_str:
                tsapp_set_mapping_verbose(AppName,TLIBApplicationChannelType.APP_LIN,FCount,mapping['LIN']['HW_Names'][i].encode('utf8'),3,HW_dict[mapping['LIN']['HW_Names'][i]],hw_sub_index,int(chn),True)
                FCount += 1
    else:
        tsapp_set_lin_channel_count(0)
    if 'Flexray' in mapping and "CHNCount"in mapping['Flexray'] and "HW_Names"in mapping['Flexray'] and "HW_Chns"in mapping['Flexray']:
        tsapp_set_flexray_channel_count(mapping['Flexray']['CHNCount'])
        HW_Names_len = len(mapping['Flexray']['HW_Names'])
        HW_Chns_len = len(mapping['Flexray']['HW_Chns'])
        if(HW_Names_len != HW_Chns_len):
            raise Exception("Length of HW_Names and HW_Chns must match")
        Mapping_channel_count = 0
        for i in range(HW_Chns_len):
            Mapping_channel_count += len(mapping['Flexray']['HW_Chns'][i].split(','))
        if Mapping_channel_count>mapping['Flexray']['CHNCount']:
            raise Exception("Number of channels in mapping is higher than number of channels on the board")
        FCount = 0
        hw = []
        for i in range(HW_Names_len):
            hw.append(mapping['Flexray']['HW_Names'][i])
            hw_sub_index = hw.count(mapping['Flexray']['HW_Names'][i]) - 1
            chn_str = mapping['Flexray']['HW_Chns'][i].split(',')
            for chn in chn_str:
                tsapp_set_mapping_verbose(AppName,TLIBApplicationChannelType.APP_FlexRay,FCount,mapping['Flexray']['HW_Names'][i].encode('utf8'),3,HW_dict[mapping['Flexray']['HW_Names'][i]],hw_sub_index,int(chn),True)
                FCount += 1
    else:
        tsapp_set_flexray_channel_count(0)
def send_msg(msg:TLIBCAN or TLIBCANFD or TLIBLIN or TLIBFlexray,is_async = True,is_cycle = False,timeout = 0.1):
    if isinstance(msg,PCAN or TLIBCAN):
        if is_cycle:
            return tsapp_add_cyclic_msg_can(msg,timeout*1000)
        elif is_async:
            return tsapp_transmit_can_async(msg)
        return tsapp_transmit_can_sync(msg,timeout*1000)
    elif isinstance(msg,PCANFD or TLIBCANFD):
        if is_cycle:
            return tsapp_add_cyclic_msg_canfd(msg,timeout*1000)
        elif is_async:
            return tsapp_transmit_canfd_async(msg)
        return tsapp_transmit_canfd_sync(msg,timeout*1000)
    elif isinstance(msg,PLIN or TLIBLIN):
        if is_async:
            return tsapp_transmit_lin_async(msg)
        return tsapp_transmit_lin_sync(msg,timeout*1000)
    elif isinstance(msg,PFlexray or TLIBFlexray):
        if is_async:
            return tsapp_transmit_flexray_async(msg)
        return tsapp_transmit_flexray_async(msg,timeout*1000)
def del_cycle_msg(msg:TLIBCAN or TLIBCANFD,is_all_cycle_msg:False):
    if is_all_cycle_msg:
        return tsapp_delete_cyclic_msgs()
    if isinstance(msg,TLIBCAN or PCAN):
        return tsapp_delete_cyclic_msg_can(msg)
    elif isinstance(msg,TLIBCANFD or PCANFD):
        return tsapp_delete_cyclic_msg_canfd(msg)
def clear_fifo_buffer(Achannel:int,msgType:MSGType):
    if msgType == MSGType.CANMSG:
        return tsfifo_clear_can_receive_buffers(Achannel)
    if msgType == MSGType.CANFDMSG:
        return tsfifo_clear_canfd_receive_buffers(Achannel)
    if msgType == MSGType.LINMSG:
        return tsfifo_clear_lin_receive_buffers(Achannel)
    if msgType == MSGType.FlexrayMSG:
        return tsfifo_clear_flexray_receive_buffers(Achannel)
def recv_msg(channelidx:CHANNEL_INDEX,msgType:MSGType,is_includeTX:False,timeout=0.1):
    if msgType == MSGType.CANMSG:
        start_time = time.perf_counter()  
        Msg_list = (TLIBCAN*1)()
        while time.perf_counter() - start_time < timeout:
            buffer_size = s32(1)
            ret = tsfifo_receive_can_msgs(Msg_list,buffer_size,channelidx,is_includeTX)
            if ret == 0 and buffer_size == 1:
                return Msg_list[0]
        return None  # Timed out or failed to receive message.
    elif msgType == MSGType.CANFDMSG:
        start_time = time.perf_counter()  
        Msg_list = (TLIBCANFD*1)()
        while time.perf_counter() - start_time < timeout:
            buffer_size = s32(1)
            ret = tsfifo_receive_canfd_msgs(Msg_list,buffer_size,channelidx,is_includeTX)
            if ret == 0 and buffer_size == 1:
                return Msg_list[0]
        return None  # Timed out or failed to receive message.
    elif msgType == MSGType.LINMSG:
        start_time = time.perf_counter()  # Time when the message was first received.
        Msg_list = (TLIBLIN*1)()
        while time.perf_counter() - start_time < timeout:
            buffer_size = s32(1)
            ret = tsfifo_receive_lin_msgs(Msg_list,buffer_size,channelidx,is_includeTX)
            if ret == 0 and buffer_size == 1:
                return Msg_list[0]
        return None  # Timed out or failed to receive message.
    elif msgType == MSGType.FlexrayMSG:
        start_time = time.perf_counter()  # Time when the message was first received.
        Msg_list = (TLIBFlexray*1)()
        while time.perf_counter() - start_time < timeout:
            buffer_size = s32(1)
            ret = tsfifo_receive_flexray_msgs(Msg_list,buffer_size,channelidx,is_includeTX)
            if ret == 0 and buffer_size == 1:
                return Msg_list[0]
        return None  # Timed out or failed to receive message.
def recv_msgs(channelidx:CHANNEL_INDEX,msgType:MSGType,Anumber:int,is_includeTX:False,timeout=0.1):  
    # Receive messages from a TSFIFO.  Blocks until a message is available.  Return a list of messages.  If no messages are available, return None. 
    if msgType == MSGType.CANMSG:
        start_time = time.perf_counter()  
        Msg_list = (TLIBCAN*Anumber)()
        while time.perf_counter() - start_time < timeout:
            buffer_size = s32(Anumber)
            ret = tsfifo_receive_can_msgs(Msg_list,buffer_size,channelidx,is_includeTX)
            if ret == 0 and buffer_size != 0:
                return Msg_list[0:buffer_size.value]
        return None  # Timed out or failed to receive message.
    elif msgType == MSGType.CANFDMSG:
        start_time = time.perf_counter()  
        Msg_list = (TLIBCANFD*Anumber)()
        while time.perf_counter() - start_time < timeout:
            buffer_size = s32(Anumber)
            ret = tsfifo_receive_canfd_msgs(Msg_list,buffer_size,channelidx,is_includeTX)
            if ret == 0 and buffer_size != 0:
                return Msg_list[0]
        return None  # Timed out or failed to receive message.
    elif msgType == MSGType.LINMSG:
        start_time = time.perf_counter()  # Time when the message was first received.
        Msg_list = (TLIBLIN*Anumber)()
        while time.perf_counter() - start_time < timeout:
            buffer_size = s32(Anumber)
            ret = tsfifo_receive_lin_msgs(Msg_list,buffer_size,channelidx,is_includeTX)
            if ret == 0 and buffer_size != 0:
                return Msg_list[0]
        return None  # Timed out or failed to receive message.
    elif msgType == MSGType.FlexrayMSG:
        start_time = time.perf_counter()  # Time when the message was first received.
        Msg_list = (TLIBFlexray*Anumber)()
        while time.perf_counter() - start_time < timeout:
            buffer_size = s32(Anumber)
            ret = tsfifo_receive_flexray_msgs(Msg_list,buffer_size,channelidx,is_includeTX)
            if ret == 0 and buffer_size != 0:
                return Msg_list[0]
        return None  # Timed out or failed to receive message.
def get_db_info(msgType:MSGType,db_idx:int):
    """
    获取的dict 结构如下：
    db:
        ECU0:
            TX_Frames:
                    Frame0:
                        signls
                    Frame1:
                        signls
        ECU1:
            RX_Frames:
                    Frame0:
                        signls
                    Frame1:
                        signls
    """
    db_info = {}
    if msgType == MSGType.CANMSG or msgType == MSGType.CANFDMSG :
        db = TDBProperties()
        db.FDBIndex = db_idx
        tsdb_get_can_db_properties_by_index(db)
        for ecu_idx in range(db.FECUCount):
            db_ecu = TDBECUProperties()
            db_ecu.FDBIndex = db_idx
            db_ecu.FECUIndex = ecu_idx
            tsdb_get_can_db_ecu_properties_by_index(db_ecu)
            db_info[db_ecu.FName] = {}
            db_info[db_ecu.FName]['TX'] = {}
            db_info[db_ecu.FName]['RX'] = {}
            for TXframe_idx in range(db_ecu.FTxFrameCount):
                db_tx_frame = TDBFrameProperties()
                db_tx_frame.FDBIndex = db_idx
                db_tx_frame.FECUIndex = ecu_idx
                db_tx_frame.FFrameIndex = TXframe_idx
                db_tx_frame.FIsTx = True
                tsdb_get_can_db_frame_properties_by_index(db_tx_frame)
                db_info[db_ecu.FName]['TX'][db_tx_frame.FName] = {}
                db_info[db_ecu.FName]['TX'][db_tx_frame.FName]['FCANIsDataFrame'] = db_tx_frame.FCANIsDataFrame
                db_info[db_ecu.FName]['TX'][db_tx_frame.FName]['FCANIsStdFrame'] = db_tx_frame.FCANIsStdFrame
                db_info[db_ecu.FName]['TX'][db_tx_frame.FName]['FCANIsEdl'] = db_tx_frame.FCANIsEdl
                db_info[db_ecu.FName]['TX'][db_tx_frame.FName]['FCANIsBrs'] = db_tx_frame.FCANIsBrs
                db_info[db_ecu.FName]['TX'][db_tx_frame.FName]['FIdentifier'] = db_tx_frame.FCANIdentifier
                db_info[db_ecu.FName]['TX'][db_tx_frame.FName]['FDLC'] = db_tx_frame.FCANDLC
                db_info[db_ecu.FName]['TX'][db_tx_frame.FName]['Signals'] = {}
                for Signal_idx in range(db_tx_frame.FSignalCount):
                    db_frame_signal = TDBSignalProperties()
                    db_frame_signal.FDBIndex = db_idx
                    db_frame_signal.FECUIndex = ecu_idx
                    db_frame_signal.FFrameIndex = TXframe_idx
                    db_frame_signal.FSignalIndex = Signal_idx
                    db_frame_signal.FIsTx = True
                    tsdb_get_can_db_signal_properties_by_index(db_frame_signal)
                    db_info[db_ecu.FName]['TX'][db_tx_frame.FName]['Signals'][db_frame_signal.FName] = {}
                    db_info[db_ecu.FName]['TX'][db_tx_frame.FName]['Signals'][db_frame_signal.FName]['def'] = db_frame_signal.FCANSignal
                    db_info[db_ecu.FName]['TX'][db_tx_frame.FName]['Signals'][db_frame_signal.FName]['value'] = db_frame_signal.FInitValue
                    del db_frame_signal
                del db_tx_frame
            for RXframe_idx in range(db_ecu.FRxFrameCount):
                db_rx_frame = TDBFrameProperties()
                db_rx_frame.FDBIndex = db_idx
                db_rx_frame.FECUIndex = ecu_idx
                db_rx_frame.FFrameIndex = RXframe_idx
                db_rx_frame.FIsTx = False
                tsdb_get_can_db_frame_properties_by_index(db_rx_frame)
                db_info[db_ecu.FName]['RX'][db_rx_frame.FName] = {}
                db_info[db_ecu.FName]['RX'][db_rx_frame.FName]['FCANIsDataFrame'] = db_rx_frame.FCANIsDataFrame
                db_info[db_ecu.FName]['RX'][db_rx_frame.FName]['FCANIsStdFrame'] = db_rx_frame.FCANIsStdFrame
                db_info[db_ecu.FName]['RX'][db_rx_frame.FName]['FCANIsEdl'] = db_rx_frame.FCANIsEdl
                db_info[db_ecu.FName]['RX'][db_rx_frame.FName]['FCANIsBrs'] = db_rx_frame.FCANIsBrs
                db_info[db_ecu.FName]['RX'][db_rx_frame.FName]['FIdentifier'] = db_rx_frame.FCANIdentifier
                db_info[db_ecu.FName]['RX'][db_rx_frame.FName]['FDLC'] = db_rx_frame.FCANDLC
                db_info[db_ecu.FName]['RX'][db_rx_frame.FName]['Signals'] = {}
                for Signal_idx in range(db_rx_frame.FSignalCount):
                    db_frame_signal = TDBSignalProperties()
                    db_frame_signal.FDBIndex = db_idx
                    db_frame_signal.FECUIndex = ecu_idx
                    db_frame_signal.FFrameIndex = RXframe_idx
                    db_frame_signal.FSignalIndex = Signal_idx
                    db_frame_signal.FIsTx = False
                    tsdb_get_can_db_signal_properties_by_index(db_frame_signal)
                    db_info[db_ecu.FName]['RX'][db_rx_frame.FName]['Signals'][db_frame_signal.FName] = {}
                    db_info[db_ecu.FName]['RX'][db_rx_frame.FName]['Signals'][db_frame_signal.FName]['def'] = db_frame_signal.FCANSignal
                    db_info[db_ecu.FName]['RX'][db_rx_frame.FName]['Signals'][db_frame_signal.FName]['value'] = db_frame_signal.FInitValue
                    del db_frame_signal
                del db_rx_frame
            del db_ecu
    if msgType == MSGType.LINMSG:
        db = TDBProperties()
        db.FDBIndex = db_idx
        tsdb_get_lin_db_properties_by_index(db)
        for ecu_idx in range(db.FECUCount):
            db_ecu = TDBECUProperties()
            db_ecu.FDBIndex = db_idx
            db_ecu.FECUIndex = ecu_idx
            tsdb_get_lin_db_ecu_properties_by_index(db_ecu)
            db_info[db_ecu.FName] = {}
            db_info[db_ecu.FName]['TX'] = {}
            db_info[db_ecu.FName]['RX'] = {}
            for TXframe_idx in range(db_ecu.FTxFrameCount):
                db_tx_frame = TDBFrameProperties()
                db_tx_frame.FDBIndex = db_idx
                db_tx_frame.FECUIndex = ecu_idx
                db_tx_frame.FFrameIndex = TXframe_idx
                db_tx_frame.FIsTx = True
                tsdb_get_lin_db_frame_properties_by_index(db_tx_frame)
                db_info[db_ecu.FName]['TX'][db_tx_frame.FName] = {}
                db_info[db_ecu.FName]['TX'][db_tx_frame.FName]['FIdentifier'] = db_tx_frame.FLINIdentifier
                db_info[db_ecu.FName]['TX'][db_tx_frame.FName]['FDLC'] = db_tx_frame.FLINDLC
                db_info[db_ecu.FName]['TX'][db_tx_frame.FName]['Signals'] = {}
                for Signal_idx in range(db_tx_frame.FSignalCount):
                    db_frame_signal = TDBSignalProperties()
                    db_frame_signal.FDBIndex = db_idx
                    db_frame_signal.FECUIndex = ecu_idx
                    db_frame_signal.FFrameIndex = TXframe_idx
                    db_frame_signal.FSignalIndex = Signal_idx
                    db_frame_signal.FIsTx = True
                    tsdb_get_lin_db_signal_properties_by_index(db_frame_signal)
                    db_info[db_ecu.FName]['TX'][db_tx_frame.FName]['Signals'][db_frame_signal.FName] = {}
                    db_info[db_ecu.FName]['TX'][db_tx_frame.FName]['Signals'][db_frame_signal.FName]['def'] = db_frame_signal.FLINSignal
                    db_info[db_ecu.FName]['TX'][db_tx_frame.FName]['Signals'][db_frame_signal.FName]['value'] = db_frame_signal.FInitValue
                    del db_frame_signal
                del db_tx_frame
            for RXframe_idx in range(db_ecu.FRxFrameCount):
                db_rx_frame = TDBFrameProperties()
                db_rx_frame.FDBIndex = db_idx
                db_rx_frame.FECUIndex = ecu_idx
                db_rx_frame.FFrameIndex = RXframe_idx
                db_rx_frame.FIsTx = False
                tsdb_get_lin_db_frame_properties_by_index(db_rx_frame)
                db_info[db_ecu.FName]['RX'][db_rx_frame.FName] = {}
                db_info[db_ecu.FName]['RX'][db_rx_frame.FName]['FIdentifier'] = db_rx_frame.FLINIdentifier
                db_info[db_ecu.FName]['RX'][db_rx_frame.FName]['FDLC'] = db_rx_frame.FLINDLC
                db_info[db_ecu.FName]['RX'][db_rx_frame.FName]['Signals'] = {}
                for Signal_idx in range(db_rx_frame.FSignalCount):
                    db_frame_signal = TDBSignalProperties()
                    db_frame_signal.FDBIndex = db_idx
                    db_frame_signal.FECUIndex = ecu_idx
                    db_frame_signal.FFrameIndex = RXframe_idx
                    db_frame_signal.FSignalIndex = Signal_idx
                    db_frame_signal.FIsTx = False
                    tsdb_get_lin_db_signal_properties_by_index(db_frame_signal)
                    db_info[db_ecu.FName]['RX'][db_rx_frame.FName]['Signals'][db_frame_signal.FName] = {}
                    db_info[db_ecu.FName]['RX'][db_rx_frame.FName]['Signals'][db_frame_signal.FName]['def'] = db_frame_signal.FLINSignal
                    db_info[db_ecu.FName]['RX'][db_rx_frame.FName]['Signals'][db_frame_signal.FName]['value'] = db_frame_signal.FInitValue
                    del db_frame_signal
                del db_rx_frame
            del db_ecu
    if msgType == MSGType.FlexrayMSG:
        db = TDBProperties()
        db.FDBIndex = db_idx
        tsdb_get_flexray_db_properties_by_index(db)
        for ecu_idx in range(db.FECUCount):
            db_ecu = TDBECUProperties()
            db_ecu.FDBIndex = db_idx
            db_ecu.FECUIndex = ecu_idx
            tsdb_get_flexray_db_ecu_properties_by_index(db_ecu)
            db_info[db_ecu.FName] = {}
            db_info[db_ecu.FName]['TX'] = {}
            db_info[db_ecu.FName]['RX'] = {}
            for TXframe_idx in range(db_ecu.FTxFrameCount):
                db_tx_frame = TDBFrameProperties()
                db_tx_frame.FDBIndex = db_idx
                db_tx_frame.FECUIndex = ecu_idx
                db_tx_frame.FFrameIndex = TXframe_idx
                db_tx_frame.FIsTx = True
                tsdb_get_flexray_db_frame_properties_by_index(db_tx_frame)
                db_info[db_ecu.FName]['TX'][db_tx_frame.FName] = {}
                db_info[db_ecu.FName]['TX'][db_tx_frame.FName]['FSlotId'] = db_tx_frame.FFRSlotId
                db_info[db_ecu.FName]['TX'][db_tx_frame.FName]['FBaseCycle'] = db_tx_frame.FFRBaseCycle
                db_info[db_ecu.FName]['TX'][db_tx_frame.FName]['FCycleRepetition'] = db_tx_frame.FFRCycleRepetition
                db_info[db_ecu.FName]['TX'][db_tx_frame.FName]['FDLC'] = db_tx_frame.FFRDLC
                db_info[db_ecu.FName]['TX'][db_tx_frame.FName]['Signals'] = {}
                for Signal_idx in range(db_tx_frame.FSignalCount):
                    db_frame_signal = TDBSignalProperties()
                    db_frame_signal.FDBIndex = db_idx
                    db_frame_signal.FECUIndex = ecu_idx
                    db_frame_signal.FFrameIndex = TXframe_idx
                    db_frame_signal.FSignalIndex = Signal_idx
                    db_frame_signal.FIsTx = True
                    tsdb_get_flexray_db_signal_properties_by_index(db_frame_signal)
                    db_info[db_ecu.FName]['TX'][db_tx_frame.FName]['Signals'][db_frame_signal.FName] = {}
                    db_info[db_ecu.FName]['TX'][db_tx_frame.FName]['Signals'][db_frame_signal.FName]['def'] = db_frame_signal.FFlexRaySignal
                    db_info[db_ecu.FName]['TX'][db_tx_frame.FName]['Signals'][db_frame_signal.FName]['value'] = db_frame_signal.FInitValue
                    del db_frame_signal
                del db_tx_frame
            for RXframe_idx in range(db_ecu.FRxFrameCount):
                db_rx_frame = TDBFrameProperties()
                db_rx_frame.FDBIndex = db_idx
                db_rx_frame.FECUIndex = ecu_idx
                db_rx_frame.FFrameIndex = RXframe_idx
                db_rx_frame.FIsTx = False
                tsdb_get_flexray_db_frame_properties_by_index(db_rx_frame)
                db_info[db_ecu.FName]['RX'][db_rx_frame.FName] = {}
                db_info[db_ecu.FName]['RX'][db_rx_frame.FName]['FSlotId'] = db_rx_frame.FFRSlotId
                db_info[db_ecu.FName]['RX'][db_rx_frame.FName]['FBaseCycle'] = db_rx_frame.FFRBaseCycle
                db_info[db_ecu.FName]['RX'][db_rx_frame.FName]['FCycleRepetition'] = db_rx_frame.FFRCycleRepetition
                db_info[db_ecu.FName]['RX'][db_rx_frame.FName]['FDLC'] = db_rx_frame.FFRDLC
                db_info[db_ecu.FName]['RX'][db_rx_frame.FName]['Signals'] = {}
                for Signal_idx in range(db_rx_frame.FSignalCount):
                    db_frame_signal = TDBSignalProperties()
                    db_frame_signal.FDBIndex = db_idx
                    db_frame_signal.FECUIndex = ecu_idx
                    db_frame_signal.FFrameIndex = RXframe_idx
                    db_frame_signal.FSignalIndex = Signal_idx
                    db_frame_signal.FIsTx = False
                    tsdb_get_flexray_db_signal_properties_by_index(db_frame_signal)
                    db_info[db_ecu.FName]['RX'][db_rx_frame.FName]['Signals'][db_frame_signal.FName] = {}
                    db_info[db_ecu.FName]['RX'][db_rx_frame.FName]['Signals'][db_frame_signal.FName]['def'] = db_frame_signal.FFlexRaySignal
                    db_info[db_ecu.FName]['RX'][db_rx_frame.FName]['Signals'][db_frame_signal.FName]['value'] = db_frame_signal.FInitValue
                    del db_frame_signal
                del db_rx_frame
            del db_ecu
    return db_info
def get_db_frame_info(msgType:MSGType,db_idx:int):
    """
    获取的dict 结构如下：
    Frame0:
        signls
    Frame1:
        signls
    Frame2:
        signls
    Frame3:
        signls
        ...
    FrameN:
        signls
    """
    db = TDBProperties()
    db.FDBIndex = db_idx
    if msgType == MSGType.FlexrayMSG:
        tsdb_get_flexray_db_properties_by_index(db)
        Frame = {}
        for Frame_id in range(db.FFrameCount):
            frame = TDBFrameProperties()
            tsdb_get_flexray_db_frame_properties_by_db_index(db_idx,Frame_id,frame)
            Frame[frame.FName] ={}
            Frame[frame.FName]['FSlotId'] = frame.FFRSlotId
            Frame[frame.FName]['FBaseCycle'] = frame.FFRBaseCycle
            Frame[frame.FName]['FCycleRepetition'] = frame.FFRCycleRepetition
            Frame[frame.FName]['FDLC'] = frame.FFRDLC
            Frame[frame.FName]['Signals'] = {}
            for singal_index in range(frame.FSignalCount):
                Signal = TDBSignalProperties()
                tsdb_get_flexray_db_signal_properties_by_frame_index(db_idx,Frame_id,singal_index,Signal)
                Frame[frame.FName]['Signals'][Signal.FName] = {}
                Frame[frame.FName]['Signals'][Signal.FName]['def'] =Signal.FFlexRaySignal
                Frame[frame.FName]['Signals'][Signal.FName]['value'] = 0
                del Signal
            del frame
    elif msgType == MSGType.CANMSG or msgType == MSGType.CANFDMSG:
        tsdb_get_can_db_properties_by_index(db)
        Frame = {}
        for Frame_id in range(db.FFrameCount):
            frame = TDBFrameProperties()
            tsdb_get_can_db_frame_properties_by_db_index(db_idx,Frame_id,frame)
            Frame[frame.FName] ={}
            Frame[frame.FName]['FCANIsDataFrame'] = frame.FCANIsDataFrame
            Frame[frame.FName]['FCANIsStdFrame'] = frame.FCANIsStdFrame
            Frame[frame.FName]['FCANIsEdl'] = frame.FCANIsEdl
            Frame[frame.FName]['FCANIsBrs'] = frame.FCANIsBrs
            Frame[frame.FName]['FIdentifier'] = frame.FCANIdentifier
            Frame[frame.FName]['FDLC'] = frame.FCANDLC
            Frame[frame.FName]['Signals'] = {}
            for singal_index in range(frame.FSignalCount):
                Signal = TDBSignalProperties()
                tsdb_get_can_db_signal_properties_by_frame_index(db_idx,Frame_id,singal_index,Signal)
                Frame[frame.FName]['Signals'][Signal.FName] = {}
                Frame[frame.FName]['Signals'][Signal.FName]['def'] = Signal.FCANSignal
                Frame[frame.FName]['Signals'][Signal.FName]['value'] = 0
                del Signal
            del frame
    elif msgType == MSGType.LINMSG :
        tsdb_get_lin_db_properties_by_index(db)
        Frame = {}
        for Frame_id in range(db.FFrameCount):
            frame = TDBFrameProperties()
            tsdb_get_lin_db_frame_properties_by_db_index(db_idx,Frame_id,frame)
            Frame[frame.FName] ={}
            Frame[frame.FName]['FIdentifier'] = frame.FLINIdentifier
            Frame[frame.FName]['FDLC'] = frame.FLINDLC
            Frame[frame.FName]['Signals'] = {}
            for singal_index in range(frame.FSignalCount):
                Signal = TDBSignalProperties()
                tsdb_get_lin_db_signal_properties_by_frame_index(db_idx,Frame_id,singal_index,Signal)
                Frame[frame.FName]['Signals'][Signal.FName] = {}
                Frame[frame.FName]['Signals'][Signal.FName]['def'] = Signal.FLINSignal
                Frame[frame.FName]['Signals'][Signal.FName]['value'] = 0
                del Signal
            del frame
    return Frame
def get_signals_value(Msg_info:dict,msg:TLIBCAN or TLIBCANFD or TLIBLIN or TLIBFlexray):
    """
    Msg_info:为get_db_info 或者 get_db_frame_info中的Frame字典
    比如:1、get_db_info 得到的字典中的 db_info['ecu1']['TX']['Frame1']
        2、get_db_frame_info 得到的字典的 Frame_info['Frame1']
    """
    if isinstance(msg,TLIBCANFD) or isinstance(msg,TLIBCAN) or isinstance(msg,PCANFD) or isinstance(msg,PCAN):
        if isinstance(Msg_info, dict) and (Msg_info['FIdentifier'] == msg.FIdentifier):
            value = {}
            for key in Msg_info['Signals']:
                value[key] = tscom_get_can_signal_value(Msg_info['Signals'][key]['def'],msg.FData)
                Msg_info['Signals'][key]['value'] = value[key]
            return value
    elif isinstance(msg,PLIN) or isinstance(msg,TLIBLIN):
        if isinstance(Msg_info, dict)and (Msg_info['FLINIdentifier'] == msg.FIdentifier):
            value = {}
            for key in Msg_info:
                value[key] = tscom_get_lin_signal_value(Msg_info['Signals'][key]['def'],msg.FData) 
                Msg_info['Signals'][key]['value'] = value[key]
            return value   
    elif isinstance(msg,PFlexray)or isinstance(msg,TLIBFlexray):
        if isinstance(Msg_info, dict) and (Msg_info['FFRSlotId'] == msg.FFSlotId and msg.FCycleNumber % Msg_info['FFRCycleRepetition'] == Msg_info['FFRBaseCycle']):
            value = {}
            for key in Msg_info['Signals']:
                value[key] = tscom_get_flexray_signal_value(Msg_info['Signals'][key]['def'],msg.FData)
                Msg_info['Signals'][key]['value'] = value[key]
            return value 
    return None  # if not supported type or not supported msg type, return None
def set_signals_value(Msg_info:dict,msg:TLIBCAN or TLIBCANFD or TLIBLIN or TLIBFlexray):
    """
    Msg_info:为get_db_info 或者 get_db_frame_info中的Frame字典
    比如:1、get_db_info 得到的字典中的 db_info['ecu1']['TX']['Frame1']
        2、get_db_frame_info 得到的字典的 Frame_info['Frame1']
    """
    if isinstance(msg,TLIBCANFD) or isinstance(msg,TLIBCAN) or isinstance(msg,PCANFD) or isinstance(msg,PCAN):
        if isinstance(Msg_info, dict) and (Msg_info['FIdentifier'] == msg.FIdentifier):
            msg.FDLC = Msg_info['FDLC']
            for key in Msg_info['Signals']:
                tscom_set_can_signal_value(Msg_info['Signals'][key]['def'],msg.FData,Msg_info['Signals'][key]['value'])
    elif isinstance(msg,PLIN) or isinstance(msg,TLIBLIN):
        if isinstance(Msg_info, dict) and (Msg_info['FIdentifier'] == msg.FIdentifier):
            msg.FDLC = Msg_info['FDLC']
            for key in Msg_info:
                tscom_set_lin_signal_value(Msg_info['Signals'][key]['def'],msg.FData,Msg_info['Signals'][key]['value'])  
    elif isinstance(msg,PFlexray)or isinstance(msg,TLIBFlexray):
        if isinstance(Msg_info, dict) and (Msg_info['FSlotId'] == msg.FFSlotId and msg.FCycleNumber % Msg_info['FCycleRepetition'] == Msg_info['FBaseCycle']):
            msg.FDLC = Msg_info['FDLC']
            for key in Msg_info['Signals']:
                tscom_set_flexray_signal_value(Msg_info['Signals'][key]['def'],msg.FData,Msg_info['Signals'][key]['value'])  
    return None  # if not supported type or not supported msg type, return None


if __name__ == "__main__":

    initialize_lib_tsmaster(b"TSMaster")
    set_mapping(mapping)
    ACAN = TLIBCANFD(FIdentifier= 0x701,FDLC=9,FData=[1,23,4,2,5,6,7])
    can_db_info = get_db_info(MSGType.CANMSG,0)
    RET = get_signals_value(can_db_info[b'Engine']['TX'][b'FallbackMessage'],ACAN)
    print(RET)
    for key in can_db_info[b'Engine']['TX'][b'FallbackMessage']['Signals']:
        can_db_info[b'Engine']['TX'][b'FallbackMessage']['Signals'][key]['value'] = 1
    set_signals_value(can_db_info[b'Engine']['TX'][b'FallbackMessage'],ACAN)
    print(ACAN)
    RET = get_signals_value(can_db_info[b'Engine']['TX'][b'FallbackMessage'],ACAN)
    print(RET)
    
    can_info = get_db_frame_info(MSGType.CANMSG,0)
    RET = get_signals_value(can_info[b'FallbackMessage'],ACAN)
    print(RET)
    for key in can_info[b'FallbackMessage']['Signals']:
        can_info[b'FallbackMessage']['Signals'][key]['value'] = 100
    set_signals_value(can_info[b'FallbackMessage'],ACAN)

    print(ACAN)

    finalize_lib_tsmaster()
