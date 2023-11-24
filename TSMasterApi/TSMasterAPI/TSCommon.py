'''
Author: seven 865762826@qq.com
Date: 2023-04-21 11:59:15
LastEditors: seven 865762826@qq.com
LastEditTime: 2023-11-24 09:38:36
'''
from .TSDirver import *
from .TSStructure import *  
from .TSEnumdefine import *  
from .TSFibex_parse import * 

# Common Functions





tsapp_get_error_description = dll.tsapp_get_error_description
tsapp_get_error_description.argtypes = [s32,charpp]
tsapp_get_error_description.restype  = TS_ReturnType 


def check_status_operation(result, function, arguments):
    """Check the status and raise """
    if result == 97:
        ret = c_char_p()
        tsapp_get_error_description(result, ret)
        print("TSDriverOperationError: " + str(function.__name__) + "(" + str(arguments) + ") returned " + str(result) + ": " + str(ret.value))
    return result

# 初始化函数 API函数使用之前 必须调用该函数 否则无法正常使用 在工程起始时 调用
initialize_lib_tsmaster = dll.initialize_lib_tsmaster
# APPName = b'TSMaster'
initialize_lib_tsmaster.argtypes = [c_char_p]
initialize_lib_tsmaster.restype = TS_ReturnType  
initialize_lib_tsmaster.errcheck = check_status_operation
# 初始化函数 API函数使用之前 必须调用该函数 否则无法正常使用 在工程起始时 与initialize_lib_tsmaster存在区别为 该函数可直接载入TSMaster工程配置
initialize_lib_tsmaster_with_project = 	dll.initialize_lib_tsmaster_with_project
# appname = b'TSMaster' project_file = b'D:/test'
initialize_lib_tsmaster_with_project.argtypes = [c_char_p,c_char_p]
initialize_lib_tsmaster_with_project.restype = TS_ReturnType 
initialize_lib_tsmaster_with_project.errcheck = check_status_operation
# 释放函数 与 initialize_lib_tsmaster 或者 initialize_lib_tsmaster_with_project 成对出现 在工程结束后 调用
finalize_lib_tsmaster = dll.finalize_lib_tsmaster
finalize_lib_tsmaster.argtypes = []
finalize_lib_tsmaster.restype = None 

# 获取当前应用程序名
tsapp_get_current_application = dll.tsapp_get_current_application
tsapp_get_current_application.argtypes = [charpp]
tsapp_get_current_application.restype = TS_ReturnType
tsapp_get_current_application.errcheck = check_status_operation
# 设置当前应用程序名
tsapp_set_current_application = dll.tsapp_set_current_application
tsapp_set_current_application.argtypes = [c_char_p]
tsapp_set_current_application.restype = TS_ReturnType
tsapp_set_current_application.errcheck = check_status_operation
# 设置当前应用程序CAN 通道数量
tsapp_set_can_channel_count = dll.tsapp_set_can_channel_count
tsapp_set_can_channel_count.argtypes = [s32]
tsapp_set_can_channel_count.restype = TS_ReturnType
tsapp_set_can_channel_count.errcheck = check_status_operation

# 获取当前应用程序CAN 通道数量
tsapp_get_can_channel_count = dll.tsapp_get_can_channel_count
tsapp_get_can_channel_count.argtypes = [ps32]
tsapp_get_can_channel_count.restype = TS_ReturnType
tsapp_get_can_channel_count.errcheck = check_status_operation

# 设置当前应用程序LIN 通道数量
tsapp_set_lin_channel_count = dll.tsapp_set_lin_channel_count
tsapp_set_lin_channel_count.argtypes = [s32]
tsapp_set_lin_channel_count.restype = TS_ReturnType
tsapp_set_lin_channel_count.errcheck = check_status_operation

# 获取当前应用程序LIN 通道数量
tsapp_get_lin_channel_count = dll.tsapp_get_lin_channel_count
tsapp_get_lin_channel_count.argtypes = [ps32]
tsapp_get_lin_channel_count.restype = TS_ReturnType
tsapp_get_lin_channel_count.errcheck = check_status_operation

# 设置当前应用程序Flexray 通道数量
tsapp_set_flexray_channel_count = dll.tsapp_set_flexray_channel_count
tsapp_set_flexray_channel_count.argtypes = [s32]
tsapp_set_flexray_channel_count.restype = TS_ReturnType
tsapp_set_flexray_channel_count.errcheck = check_status_operation

# 获取当前应用程序Flexray 通道数量
tsapp_get_flexray_channel_count = dll.tsapp_get_flexray_channel_count
tsapp_get_flexray_channel_count.argtypes = [ps32]
tsapp_get_flexray_channel_count.restype = TS_ReturnType
tsapp_get_flexray_channel_count.errcheck = check_status_operation

# 设置 映射关系
tsapp_set_mapping = dll.tsapp_set_mapping
tsapp_set_mapping.argtypes = [PLIBTSMapping] 	
tsapp_set_mapping.restype = TS_ReturnType 	
tsapp_set_mapping.errcheck = check_status_operation

# 获取 映射关系
tsapp_get_mapping = dll.tsapp_get_mapping
tsapp_get_mapping.argtypes = [PLIBTSMapping] 	
tsapp_get_mapping.restype = TS_ReturnType 
tsapp_get_mapping.errcheck = check_status_operation

# 设置 映射关系
tsapp_set_mapping_verbose = dll.tsapp_set_mapping_verbose
# (AppName: c_char_p, ALIBApplicationChannelType: TLIBApplicationChannelType, CHANNEL_INDEX: CHANNEL_INDEX,HW_name: c_char_p,BusToolDeviceType: s32, HW_Type: s32, HWidx:s32,AHardwareChannel: CHANNEL_INDEX,AEnableMapping: c_bool)
tsapp_set_mapping_verbose.argtypes = [c_char_p,s32,s32,c_char_p,s32,s32,s32,s32,c_bool]
tsapp_set_mapping_verbose.restype = TS_ReturnType
tsapp_set_mapping_verbose.errcheck = check_status_operation

# 删除硬件通道映射
tsapp_del_mapping_verbose = dll.tsapp_del_mapping_verbose
# (AppName: c_char_p, ALIBApplicationChannelType: TLIBApplicationChannelType, APP_Channel: CHANNEL_INDEX)
tsapp_del_mapping_verbose.argtypes = [c_char_p,s32,s32]
tsapp_del_mapping_verbose.restype = TS_ReturnType
tsapp_del_mapping_verbose.errcheck = check_status_operation

# CAN 通道参数配置
tsapp_configure_baudrate_can = dll.tsapp_configure_baudrate_can
# (APP_Channel: CHANNEL_INDEX, ABaudrateKbps: c_float, AListenOnly: c_bool,AInstallTermResistor120Ohm: c_bool)
tsapp_configure_baudrate_can.argtypes = [s32, c_float, c_bool, c_bool]
tsapp_configure_baudrate_can.restype = TS_ReturnType
tsapp_configure_baudrate_can.errcheck = check_status_operation

# CANFD 通道参数配置
tsapp_configure_baudrate_canfd = dll.tsapp_configure_baudrate_canfd
# (AIdxChn: CHANNEL_INDEX, ABaudrateArbKbps: c_float, ABaudrateDataKbps: c_float,AControllerType: s16, AControllerMode: s16,AInstallTermResistor120Ohm: c_bool)
tsapp_configure_baudrate_canfd.argtypes = [s32, c_float, c_float,s16 ,s16,c_bool]
tsapp_configure_baudrate_canfd.restype = TS_ReturnType
tsapp_configure_baudrate_canfd.errcheck = check_status_operation

# can brs 采样率设置  AOnlyListen=0表示只听模式  A120大于0表示激活终端电阻，=0表示不激活
tsapp_configure_can_regs = dll.tsapp_configure_can_regs
# (AIdxChn: CHANNEL_INDEX, ABaudrateKbps: float, ASEG1: int, ASEG2: int, APrescaler: int,ASJ2: int, AOnlyListen: int, A120: int)
tsapp_configure_can_regs.argtypes = [s32, c_float, s32,s32,s32,s32,c_bool, c_bool]
tsapp_configure_can_regs.restype = TS_ReturnType
tsapp_configure_can_regs.errcheck = check_status_operation

# canfd brs 采样率设置  A120大于0表示激活终端电阻，=0表示不激活
tsapp_configure_canfd_regs = dll.tsapp_configure_canfd_regs
# (AIdxChn: CHANNEL_INDEX, AArbBaudrateKbps: float, AArbSEG1: int, AArbSEG2: int,
                            #    AArbPrescaler: int,
                            #    AArbSJ2: int, ADataBaudrateKbps: float, ADataSEG1: int, ADataSEG2: int,
                            #    ADataPrescaler: int,
                            #    ADataSJ2: int, AControllerType: TLIBCANFDControllerType,
                            #    AControllerMode: TLIBCANFDControllerMode,
                            #    AInstallTermResistor120Ohm: int):
tsapp_configure_canfd_regs.argtypes = [s32, c_float, s32,s32,s32,s32,c_float, s32,s32,s32,s32,s32,s32, c_bool]
tsapp_configure_canfd_regs.restype = TS_ReturnType
tsapp_configure_canfd_regs.errcheck = check_status_operation

# LIN 通道参数配置
tsapp_configure_baudrate_lin = dll.tsapp_configure_baudrate_lin
# (AIdxChn: CHANNEL_INDEX, ABaudrateKbps: int, LIN_PROTOCOL: LIN_PROTOCOL)
tsapp_configure_baudrate_lin.argtypes = [s32, c_float, s32]
tsapp_configure_baudrate_lin.restype = TS_ReturnType
tsapp_configure_baudrate_lin.errcheck = check_status_operation

# 设置LIN模式
tslin_set_node_funtiontype = dll.tslin_set_node_functiontype
# (AIdxChn: CHANNEL_INDEX, TLINNodeType: T_LIN_NODE_FUNCTION)
tslin_set_node_funtiontype.argtypes=[s32, s32]
tslin_set_node_funtiontype.restype = TS_ReturnType
tslin_set_node_funtiontype.errcheck = check_status_operation

# 获取在线硬件 参数必须为变量
tsapp_enumerate_hw_devices = dll.tsapp_enumerate_hw_devices
tsapp_enumerate_hw_devices.argtypes=[ps32]
tsapp_enumerate_hw_devices.restype = TS_ReturnType
tsapp_enumerate_hw_devices.errcheck = check_status_operation

# 通过索引获取硬件（名称、描述和描述数据）
tsapp_get_hw_info_by_index = dll.tsapp_get_hw_info_by_index
tsapp_get_hw_info_by_index.argtypes=[s32,PLIBHWInfo]
tsapp_get_hw_info_by_index.restype = TS_ReturnType
tsapp_get_hw_info_by_index.errcheck = check_status_operation


# 开启fifo
tsfifo_enable_receive_fifo = dll.tsfifo_enable_receive_fifo
tsfifo_enable_receive_fifo.argtypes = []  
tsfifo_enable_receive_fifo.restype = None

# 关闭fifo
tsfifo_disable_receive_fifo = dll.tsfifo_disable_receive_fifo
tsfifo_disable_receive_fifo.argtypes = []  
tsfifo_disable_receive_fifo.restype = None

# 连接
tsapp_connect = dll.tsapp_connect
tsapp_connect.argtypes = []  
tsapp_connect.restype = TS_ReturnType
tsapp_connect.errcheck = check_status_operation

# 断开连接
tsapp_disconnect = dll.tsapp_disconnect
tsapp_disconnect.argtypes = []  
tsapp_disconnect.restype = TS_ReturnType
tsapp_disconnect.errcheck = check_status_operation

# 开始录制报文
tsapp_start_logging = dll.tsapp_start_logging
tsapp_start_logging.argtypes = [c_char_p]  
tsapp_start_logging.restype = TS_ReturnType
tsapp_start_logging.errcheck = check_status_operation

# 停止录制报文
tsapp_stop_logging = dll.tsapp_stop_logging
tsapp_stop_logging.argtypes = []  
tsapp_stop_logging.restype = TS_ReturnType
tsapp_stop_logging.errcheck = check_status_operation

# 打开TsMaster窗口
tsapp_show_tsmaster_window = dll.tsapp_show_tsmaster_window
tsapp_show_tsmaster_window.argtypes = [c_char_p,c_bool]  
tsapp_show_tsmaster_window.restype = TS_ReturnType
tsapp_show_tsmaster_window.errcheck = check_status_operation

# 注销所有预发送事件
tsapp_unregister_pretx_events_all = dll.tsapp_unregister_pretx_events_all
tsapp_unregister_pretx_events_all.argtypes = [ps32]  
tsapp_unregister_pretx_events_all.restype = TS_ReturnType
tsapp_unregister_pretx_events_all.errcheck = check_status_operation

# 注销所有发送_接收事件
tsapp_unregister_events_all = dll.tsapp_unregister_events_all
tsapp_unregister_events_all.argtypes = [ps32]  
tsapp_unregister_events_all.restype = TS_ReturnType
tsapp_unregister_events_all.errcheck = check_status_operation

#增加应用程序
tsapp_add_application = dll.tsapp_add_application
tsapp_add_application.argtypes = [c_char_p]  
tsapp_add_application.restype = TS_ReturnType
tsapp_add_application.errcheck = check_status_operation

#删除应用程序
tsapp_del_application = dll.tsapp_del_application
tsapp_del_application.argtypes = [c_char_p]  
tsapp_del_application.restype = TS_ReturnType
tsapp_del_application.errcheck = check_status_operation

# 是否使能总线数据统计
tsapp_enable_bus_statistics = dll.tsapp_enable_bus_statistics
tsapp_enable_bus_statistics.argtypes = [c_bool] 
tsapp_enable_bus_statistics.restype = TS_ReturnType
tsapp_enable_bus_statistics.errcheck = check_status_operation

# 获取can每秒帧数，需要先使能总线统计
tsapp_get_fps_can = dll.tsapp_get_fps_can
tsapp_get_fps_can.argtypes = [s32,s32,ps32] 
tsapp_get_fps_can.restype = TS_ReturnType
tsapp_get_fps_can.errcheck = check_status_operation

# 获取canfd每秒帧数，需要先使能总线统计
tsapp_get_fps_canfd = dll.tsapp_get_fps_canfd
tsapp_get_fps_canfd.argtypes = [s32,s32,ps32] 
tsapp_get_fps_canfd.restype = TS_ReturnType
tsapp_get_fps_canfd.errcheck = check_status_operation

# 获取lin每秒帧数，需要先使能总线统计
tsapp_get_fps_lin = dll.tsapp_get_fps_lin
tsapp_get_fps_lin.argtypes = [s32,s32,ps32] 
tsapp_get_fps_lin.restype = TS_ReturnType
tsapp_get_fps_lin.errcheck = check_status_operation

# 获取硬件时间戳
tsapp_get_timestamp = dll.tsapp_get_timestamp
tsapp_get_timestamp.argtypes = [ps32] 
tsapp_get_timestamp.restype = TS_ReturnType
tsapp_get_timestamp.errcheck = check_status_operation

# 关闭错误帧fifo
tsfifo_disable_receive_error_frames = dll.tsfifo_disable_receive_error_frames
tsfifo_disable_receive_error_frames.argtypes = [] 
tsfifo_disable_receive_error_frames.restype = None

# 开启错误帧fifo
tsfifo_enable_receive_error_frames = dll.tsfifo_enable_receive_error_frames
tsfifo_enable_receive_error_frames.argtypes = [] 
tsfifo_enable_receive_error_frames.restype = None



# TSCANAPI

# CAN报文发送

# 异步单帧发送CAN报文
tsapp_transmit_can_async = dll.tsapp_transmit_can_async
tsapp_transmit_can_async.argtypes = [PCAN]  
tsapp_transmit_can_async.restype = TS_ReturnType
tsapp_transmit_can_async.errcheck = check_status_operation

# 同步单帧发送CAN报文
tsapp_transmit_can_sync = dll.tsapp_transmit_can_sync
tsapp_transmit_can_sync.argtypes = [PCAN,s32]  
tsapp_transmit_can_sync.restype = TS_ReturnType
tsapp_transmit_can_sync.errcheck = check_status_operation

# 设置CAN 信号值
tsdb_set_signal_value_can = dll.tsdb_set_signal_value_can
tsdb_set_signal_value_can.argtypes = [PCAN,c_char_p,c_char_p,double]  
tsdb_set_signal_value_can.restype = TS_ReturnType
tsdb_set_signal_value_can.errcheck = check_status_operation

# 获取信号值
tsdb_get_signal_value_can = dll.tsdb_get_signal_value_can
tsdb_get_signal_value_can.argtypes = [PCAN,c_char_p,c_char_p,pdouble]  
tsdb_get_signal_value_can.restype = TS_ReturnType
tsdb_get_signal_value_can.errcheck = check_status_operation

# 增加周期发送CAN报文
tsapp_add_cyclic_msg_can = dll.tsapp_add_cyclic_msg_can
tsapp_add_cyclic_msg_can.argtypes = [PCAN,c_float]  
tsapp_add_cyclic_msg_can.restype = TS_ReturnType
tsapp_add_cyclic_msg_can.errcheck = check_status_operation

# 删除周期发送CAN报文
tsapp_delete_cyclic_msg_can = dll.tsapp_delete_cyclic_msg_can
tsapp_delete_cyclic_msg_can.argtypes = [PCAN]  
tsapp_delete_cyclic_msg_can.restype = TS_ReturnType
tsapp_delete_cyclic_msg_can.errcheck = check_status_operation

# 异步单帧发送CANFD报文
tsapp_transmit_canfd_async = dll.tsapp_transmit_canfd_async
tsapp_transmit_canfd_async.argtypes = [PCANFD]  
tsapp_transmit_canfd_async.restype = TS_ReturnType
tsapp_transmit_canfd_async.errcheck = check_status_operation

# 同步单帧发送CANFD报文
tsapp_transmit_canfd_sync = dll.tsapp_transmit_canfd_sync
tsapp_transmit_canfd_sync.argtypes = [PCANFD,s32]  
tsapp_transmit_canfd_sync.restype = TS_ReturnType
tsapp_transmit_canfd_sync.errcheck = check_status_operation

# 设置CANFD 信号值
tsdb_set_signal_value_canfd = dll.tsdb_set_signal_value_canfd
tsdb_set_signal_value_canfd.argtypes = [PCAN,c_char_p,c_char_p,double]  
tsdb_set_signal_value_canfd.restype = TS_ReturnType
tsdb_set_signal_value_canfd.errcheck = check_status_operation

# 获取信号值
tsdb_get_signal_value_canfd = dll.tsdb_get_signal_value_canfd
tsdb_get_signal_value_canfd.argtypes = [PCANFD,c_char_p,c_char_p,pdouble]  
tsdb_get_signal_value_canfd.restype = TS_ReturnType
tsdb_get_signal_value_canfd.errcheck = check_status_operation

# 增加周期发送CANFD报文
tsapp_add_cyclic_msg_canfd = dll.tsapp_add_cyclic_msg_canfd
tsapp_add_cyclic_msg_canfd.argtypes = [PCANFD,c_float]  
tsapp_add_cyclic_msg_canfd.restype = TS_ReturnType
tsapp_add_cyclic_msg_canfd.errcheck = check_status_operation

# 删除周期发送CANFD报文
tsapp_delete_cyclic_msg_canfd = dll.tsapp_delete_cyclic_msg_canfd
tsapp_delete_cyclic_msg_canfd.argtypes = [PCANFD]  
tsapp_delete_cyclic_msg_canfd.restype = TS_ReturnType
tsapp_delete_cyclic_msg_canfd.errcheck = check_status_operation

# 删除所有周期发送报文
tsapp_delete_cyclic_msgs = dll.tsapp_delete_cyclic_msgs
tsapp_delete_cyclic_msgs.argtypes = []  
tsapp_delete_cyclic_msgs.restype = TS_ReturnType
tsapp_delete_cyclic_msgs.errcheck = check_status_operation

# CAN报文接收

# 接收can 报文
tsfifo_receive_can_msgs = dll.tsfifo_receive_can_msgs
tsfifo_receive_can_msgs.argtypes = [PCAN,ps32,s32,s32]  
tsfifo_receive_can_msgs.restype = TS_ReturnType
tsfifo_receive_can_msgs.errcheck = check_status_operation

# 获取fifo 中can报文数量
tsfifo_read_can_buffer_frame_count = dll.tsfifo_read_can_buffer_frame_count
tsfifo_read_can_buffer_frame_count.argtypes = [s32,ps32]  
tsfifo_read_can_buffer_frame_count.restype = TS_ReturnType
tsfifo_read_can_buffer_frame_count.errcheck = check_status_operation

# 获取fifo 中TX can报文数量
tsfifo_read_can_tx_buffer_frame_count = dll.tsfifo_read_can_tx_buffer_frame_count
tsfifo_read_can_tx_buffer_frame_count.argtypes = [s32,ps32]  
tsfifo_read_can_tx_buffer_frame_count.restype = TS_ReturnType
tsfifo_read_can_tx_buffer_frame_count.errcheck = check_status_operation

# 获取fifo 中RX can报文数量
tsfifo_read_can_rx_buffer_frame_count = dll.tsfifo_read_can_rx_buffer_frame_count
tsfifo_read_can_rx_buffer_frame_count.argtypes = [s32,ps32]  
tsfifo_read_can_rx_buffer_frame_count.restype = TS_ReturnType
tsfifo_read_can_rx_buffer_frame_count.errcheck = check_status_operation

# 清空 can fifo
tsfifo_clear_can_receive_buffers = dll.tsfifo_clear_can_receive_buffers
tsfifo_clear_can_receive_buffers.argtypes = [s32]  
tsfifo_clear_can_receive_buffers.restype = TS_ReturnType
tsfifo_clear_can_receive_buffers.errcheck = check_status_operation

# CAN 回调事件

# 注册预发送事件
tsapp_register_pretx_event_can = dll.tsapp_register_pretx_event_can
tsapp_register_pretx_event_can.argtypes = [ps32,OnTx_RxFUNC_CAN]  
tsapp_register_pretx_event_can.restype = TS_ReturnType
tsapp_register_pretx_event_can.errcheck = check_status_operation

# 注销预发送事件
tsapp_unregister_pretx_event_can = dll.tsapp_unregister_pretx_event_can
tsapp_unregister_pretx_event_can.argtypes = [ps32,OnTx_RxFUNC_CAN]  
tsapp_unregister_pretx_event_can.restype = TS_ReturnType
tsapp_unregister_pretx_event_can.errcheck = check_status_operation

# 注册rx_tx事件
tsapp_register_event_can = dll.tsapp_register_event_can
tsapp_register_event_can.argtypes = [ps32,OnTx_RxFUNC_CAN]  
tsapp_register_event_can.restype = TS_ReturnType
tsapp_register_event_can.errcheck = check_status_operation

# 注销rx_tx事件
tsapp_unregister_event_can = dll.tsapp_unregister_event_can
tsapp_unregister_event_can.argtypes = [ps32,OnTx_RxFUNC_CAN]  
tsapp_unregister_event_can.restype = TS_ReturnType
tsapp_unregister_event_can.errcheck = check_status_operation


# 接收canfd 报文
tsfifo_receive_canfd_msgs = dll.tsfifo_receive_canfd_msgs
tsfifo_receive_canfd_msgs.argtypes = [PCANFD,ps32,s32,s32]  
tsfifo_receive_canfd_msgs.restype = TS_ReturnType
tsfifo_receive_canfd_msgs.errcheck = check_status_operation

# 获取fifo 中canfd报文数量
tsfifo_read_canfd_buffer_frame_count = dll.tsfifo_read_canfd_buffer_frame_count
tsfifo_read_canfd_buffer_frame_count.argtypes = [s32,ps32]  
tsfifo_read_canfd_buffer_frame_count.restype = TS_ReturnType
tsfifo_read_canfd_buffer_frame_count.errcheck = check_status_operation

# 获取fifo 中TX canfd报文数量
tsfifo_read_canfd_tx_buffer_frame_count = dll.tsfifo_read_canfd_tx_buffer_frame_count
tsfifo_read_canfd_tx_buffer_frame_count.argtypes = [s32,ps32]  
tsfifo_read_canfd_tx_buffer_frame_count.restype = TS_ReturnType
tsfifo_read_canfd_tx_buffer_frame_count.errcheck = check_status_operation

# 获取fifo 中RX canfd报文数量
tsfifo_read_canfd_rx_buffer_frame_count = dll.tsfifo_read_canfd_rx_buffer_frame_count
tsfifo_read_canfd_rx_buffer_frame_count.argtypes = [s32,ps32]  
tsfifo_read_canfd_rx_buffer_frame_count.restype = TS_ReturnType
tsfifo_read_canfd_rx_buffer_frame_count.errcheck = check_status_operation

# 清空 canfd fifo
tsfifo_clear_canfd_receive_buffers = dll.tsfifo_clear_canfd_receive_buffers
tsfifo_clear_canfd_receive_buffers.argtypes = [s32]  
tsfifo_clear_canfd_receive_buffers.restype = TS_ReturnType
tsfifo_clear_canfd_receive_buffers.errcheck = check_status_operation

# CANFD 回调事件
# 注册预发送事件
tsapp_register_pretx_event_canfd = dll.tsapp_register_pretx_event_canfd
tsapp_register_pretx_event_canfd.argtypes = [ps32,OnTx_RxFUNC_CANFD]  
tsapp_register_pretx_event_canfd.restype = TS_ReturnType
tsapp_register_pretx_event_canfd.errcheck = check_status_operation

# 注销预发送事件
tsapp_unregister_pretx_event_canfd = dll.tsapp_unregister_pretx_event_canfd
tsapp_unregister_pretx_event_canfd.argtypes = [ps32,OnTx_RxFUNC_CANFD]  
tsapp_unregister_pretx_event_canfd.restype = TS_ReturnType
tsapp_unregister_pretx_event_canfd.errcheck = check_status_operation

# 注册rx_tx事件
tsapp_register_event_canfd = dll.tsapp_register_event_canfd
tsapp_register_event_canfd.argtypes = [ps32,OnTx_RxFUNC_CANFD]  
tsapp_register_event_canfd.restype = TS_ReturnType
tsapp_register_event_canfd.errcheck = check_status_operation

# 注销rx_tx事件
tsapp_unregister_event_canfd = dll.tsapp_unregister_event_canfd
tsapp_unregister_event_canfd.argtypes = [ps32,OnTx_RxFUNC_CANFD]  
tsapp_unregister_event_canfd.restype = TS_ReturnType
tsapp_unregister_event_canfd.errcheck = check_status_operation

# can db info

# 载入数据库
tsdb_load_can_db = dll.tsdb_load_can_db
tsdb_load_can_db.argtypes = [c_char_p,c_char_p,ps32]  
tsdb_load_can_db.restype = TS_ReturnType
tsdb_load_can_db.errcheck = check_status_operation

# 卸载指定数据库
tsdb_unload_can_db = dll.tsdb_unload_can_db
tsdb_unload_can_db.argtypes = [s32]  
tsdb_unload_can_db.restype = TS_ReturnType
tsdb_unload_can_db.errcheck = check_status_operation

# 卸载所有数据库
tsdb_unload_can_dbs = dll.tsdb_unload_can_dbs
tsdb_unload_can_dbs.argtypes = []  
tsdb_unload_can_dbs.restype = TS_ReturnType
tsdb_unload_can_dbs.errcheck = check_status_operation

# 获取加载的数据库数量
tsdb_get_can_db_count = dll.tsdb_get_can_db_count
tsdb_get_can_db_count.argtypes = [ps32]  
tsdb_get_can_db_count.restype = TS_ReturnType
tsdb_get_can_db_count.errcheck = check_status_operation

# 通过索引获取数据库id
tsdb_get_can_db_id = dll.tsdb_get_can_db_id
tsdb_get_can_db_id.argtypes = [s32,ps32]  
tsdb_get_can_db_id.restype = TS_ReturnType
tsdb_get_can_db_id.errcheck = check_status_operation

# 通过地址获取指定数据库的DB信息
tsdb_get_can_db_properties_by_address = dll.tsdb_get_can_db_properties_by_address
tsdb_get_can_db_properties_by_address.argtypes = [c_char_p,PDBProperties]  
tsdb_get_can_db_properties_by_address.restype = TS_ReturnType
tsdb_get_can_db_properties_by_address.errcheck = check_status_operation

# 通过索引获取指定数据库的DB信息
tsdb_get_can_db_properties_by_index = dll.tsdb_get_can_db_properties_by_index
tsdb_get_can_db_properties_by_index.argtypes = [PDBProperties]  
tsdb_get_can_db_properties_by_index.restype = TS_ReturnType
tsdb_get_can_db_properties_by_index.errcheck = check_status_operation

# 通过地址获取指定数据库的ECU信息
tsdb_get_can_db_ecu_properties_by_address = dll.tsdb_get_can_db_ecu_properties_by_address
tsdb_get_can_db_ecu_properties_by_address.argtypes = [c_char_p,PDBECUProperties]  
tsdb_get_can_db_ecu_properties_by_address.restype = TS_ReturnType
tsdb_get_can_db_ecu_properties_by_address.errcheck = check_status_operation

# 通过索引获取指定数据库的ECU信息
tsdb_get_can_db_ecu_properties_by_index = dll.tsdb_get_can_db_ecu_properties_by_index
tsdb_get_can_db_ecu_properties_by_index.argtypes = [PDBECUProperties]  
tsdb_get_can_db_ecu_properties_by_index.restype = TS_ReturnType
tsdb_get_can_db_ecu_properties_by_index.errcheck = check_status_operation

# 通过地址获取指定数据库的Frame信息
tsdb_get_can_db_frame_properties_by_address = dll.tsdb_get_can_db_frame_properties_by_address
tsdb_get_can_db_frame_properties_by_address.argtypes = [c_char_p,PDBFrameProperties]  
tsdb_get_can_db_frame_properties_by_address.restype = TS_ReturnType
tsdb_get_can_db_frame_properties_by_address.errcheck = check_status_operation

# 通过索引获取指定数据库的Frame信息
tsdb_get_can_db_frame_properties_by_index = dll.tsdb_get_can_db_frame_properties_by_index
tsdb_get_can_db_frame_properties_by_index.argtypes = [PDBFrameProperties]  
tsdb_get_can_db_frame_properties_by_index.restype = TS_ReturnType
tsdb_get_can_db_frame_properties_by_index.errcheck = check_status_operation

# 通过数据库索引获取指定数据库的Frame信息
tsdb_get_can_db_frame_properties_by_db_index = dll.tsdb_get_can_db_frame_properties_by_db_index
tsdb_get_can_db_frame_properties_by_db_index.argtypes = [s32,s32,PDBFrameProperties]  
tsdb_get_can_db_frame_properties_by_db_index.restype = TS_ReturnType
tsdb_get_can_db_frame_properties_by_db_index.errcheck = check_status_operation

# 通过地址获取指定数据库的Signal信息
tsdb_get_can_db_signal_properties_by_address = dll.tsdb_get_can_db_signal_properties_by_address
tsdb_get_can_db_signal_properties_by_address.argtypes = [c_char_p,PDBSignalProperties]  
tsdb_get_can_db_signal_properties_by_address.restype = TS_ReturnType
tsdb_get_can_db_signal_properties_by_address.errcheck = check_status_operation

# 通过索引获取指定数据库的Signal信息
tsdb_get_can_db_signal_properties_by_index = dll.tsdb_get_can_db_signal_properties_by_index
tsdb_get_can_db_signal_properties_by_index.argtypes = [PDBSignalProperties]  
tsdb_get_can_db_signal_properties_by_index.restype = TS_ReturnType
tsdb_get_can_db_signal_properties_by_index.errcheck = check_status_operation

# 通过数据库索引获取指定数据库的Signal信息
tsdb_get_can_db_signal_properties_by_db_index = dll.tsdb_get_can_db_signal_properties_by_db_index
tsdb_get_can_db_signal_properties_by_db_index.argtypes = [s32,s32,PDBSignalProperties]  
tsdb_get_can_db_signal_properties_by_db_index.restype = TS_ReturnType
tsdb_get_can_db_signal_properties_by_db_index.errcheck = check_status_operation

# 通过Frame索引获取指定数据库的Signal信息
tsdb_get_can_db_signal_properties_by_frame_index = dll.tsdb_get_can_db_signal_properties_by_frame_index
tsdb_get_can_db_signal_properties_by_frame_index.argtypes = [s32,s32,s32,PDBSignalProperties]  
tsdb_get_can_db_signal_properties_by_frame_index.restype = TS_ReturnType
tsdb_get_can_db_signal_properties_by_frame_index.errcheck = check_status_operation

# 获取报文中信号值
tscom_get_can_signal_value = dll.tscom_get_can_signal_value #函数对象
tscom_get_can_signal_value.argtypes = [PCANSignal,pu8] #指定参数类型
tscom_get_can_signal_value.restype = c_double 

# 设置报文中的信号值
tscom_set_can_signal_value = dll.tscom_set_can_signal_value #函数对象
tscom_set_can_signal_value.argtypes = [PCANSignal,pu8,double] #指定参数类型
tscom_set_can_signal_value.restype = TS_ReturnType 
tscom_set_can_signal_value.errcheck = check_status_operation

# LIN API

# LIN 发送报文

# 异步单帧发送LIN报文
tsapp_transmit_lin_async = dll.tsapp_transmit_lin_async
tsapp_transmit_lin_async.argtypes = [PLIN]  
tsapp_transmit_lin_async.restype = TS_ReturnType
tsapp_transmit_lin_async.errcheck = check_status_operation

# 同步单帧发送LIN报文
tsapp_transmit_lin_sync = dll.tsapp_transmit_lin_sync
tsapp_transmit_lin_sync.argtypes = [PLIN,s32]  
tsapp_transmit_lin_sync.restype = TS_ReturnType
tsapp_transmit_lin_sync.errcheck = check_status_operation
# LIN报文接收

# 接收LIN 报文
tsfifo_receive_lin_msgs = dll.tsfifo_receive_lin_msgs
tsfifo_receive_lin_msgs.argtypes = [PLIN,ps32,s32,s32]  
tsfifo_receive_lin_msgs.restype = TS_ReturnType
tsfifo_receive_lin_msgs.errcheck = check_status_operation

# 获取fifo 中lin报文数量
tsfifo_read_lin_buffer_frame_count = dll.tsfifo_read_lin_buffer_frame_count
tsfifo_read_lin_buffer_frame_count.argtypes = [s32,ps32]  
tsfifo_read_lin_buffer_frame_count.restype = TS_ReturnType
tsfifo_read_lin_buffer_frame_count.errcheck = check_status_operation

# 获取fifo 中TX lin报文数量
tsfifo_read_lin_tx_buffer_frame_count = dll.tsfifo_read_lin_tx_buffer_frame_count
tsfifo_read_lin_tx_buffer_frame_count.argtypes = [s32,ps32]  
tsfifo_read_lin_tx_buffer_frame_count.restype = TS_ReturnType
tsfifo_read_lin_tx_buffer_frame_count.errcheck = check_status_operation

# 获取fifo 中RX lin报文数量
tsfifo_read_lin_rx_buffer_frame_count = dll.tsfifo_read_lin_rx_buffer_frame_count
tsfifo_read_lin_rx_buffer_frame_count.argtypes = [s32,ps32]  
tsfifo_read_lin_rx_buffer_frame_count.restype = TS_ReturnType
tsfifo_read_lin_rx_buffer_frame_count.errcheck = check_status_operation

# 清空 lin fifo
tsfifo_clear_lin_receive_buffers = dll.tsfifo_clear_lin_receive_buffers
tsfifo_clear_lin_receive_buffers.argtypes = [s32]  
tsfifo_clear_lin_receive_buffers.restype = TS_ReturnType
tsfifo_clear_lin_receive_buffers.errcheck = check_status_operation

# LIN 回调事件

# 注册预发送事件
tsapp_register_pretx_event_lin = dll.tsapp_register_pretx_event_lin
tsapp_register_pretx_event_lin.argtypes = [ps32,OnTx_RxFUNC_LIN]  
tsapp_register_pretx_event_lin.restype = TS_ReturnType
tsapp_register_pretx_event_lin.errcheck = check_status_operation

# 注销预发送事件
tsapp_unregister_pretx_event_lin = dll.tsapp_unregister_pretx_event_lin
tsapp_unregister_pretx_event_lin.argtypes = [ps32,OnTx_RxFUNC_LIN]  
tsapp_unregister_pretx_event_lin.restype = TS_ReturnType
tsapp_unregister_pretx_event_lin.errcheck = check_status_operation

# 注册rx_tx事件
tsapp_register_event_lin = dll.tsapp_register_event_lin
tsapp_register_event_lin.argtypes = [ps32,OnTx_RxFUNC_LIN]  
tsapp_register_event_lin.restype = TS_ReturnType
tsapp_register_event_lin.errcheck = check_status_operation

# 注销rx_tx事件
tsapp_unregister_event_lin = dll.tsapp_unregister_event_lin
tsapp_unregister_event_lin.argtypes = [ps32,OnTx_RxFUNC_LIN]  
tsapp_unregister_event_lin.restype = TS_ReturnType
tsapp_unregister_event_lin.errcheck = check_status_operation

# lin db info

# 载入数据库
tsdb_load_lin_db = dll.tsdb_load_lin_db
tsdb_load_lin_db.argtypes = [c_char_p,c_char_p,ps32]  
tsdb_load_lin_db.restype = TS_ReturnType
tsdb_load_lin_db.errcheck = check_status_operation

# 卸载指定数据库
tsdb_unload_lin_db = dll.tsdb_unload_lin_db
tsdb_unload_lin_db.argtypes = [s32]  
tsdb_unload_lin_db.restype = TS_ReturnType
tsdb_unload_lin_db.errcheck = check_status_operation

# 卸载所有数据库
tsdb_unload_lin_dbs = dll.tsdb_unload_lin_dbs
tsdb_unload_lin_dbs.argtypes = []  
tsdb_unload_lin_dbs.restype = TS_ReturnType
tsdb_unload_lin_dbs.errcheck = check_status_operation

# 获取加载的数据库数量
tsdb_get_lin_db_count = dll.tsdb_get_lin_db_count
tsdb_get_lin_db_count.argtypes = [ps32]  
tsdb_get_lin_db_count.restype = TS_ReturnType
tsdb_get_lin_db_count.errcheck = check_status_operation

# 通过索引获取数据库id
tsdb_get_lin_db_id = dll.tsdb_get_lin_db_id
tsdb_get_lin_db_id.argtypes = [s32,ps32]  
tsdb_get_lin_db_id.restype = TS_ReturnType
tsdb_get_lin_db_id.errcheck = check_status_operation

# 通过地址获取指定数据库的DB信息
tsdb_get_lin_db_properties_by_address = dll.tsdb_get_lin_db_properties_by_address
tsdb_get_lin_db_properties_by_address.argtypes = [c_char_p,PDBProperties]  
tsdb_get_lin_db_properties_by_address.restype = TS_ReturnType
tsdb_get_lin_db_properties_by_address.errcheck = check_status_operation

# 通过索引获取指定数据库的DB信息
tsdb_get_lin_db_properties_by_index = dll.tsdb_get_lin_db_properties_by_index
tsdb_get_lin_db_properties_by_index.argtypes = [PDBProperties]  
tsdb_get_lin_db_properties_by_index.restype = TS_ReturnType
tsdb_get_lin_db_properties_by_index.errcheck = check_status_operation

# 通过地址获取指定数据库的ECU信息
tsdb_get_lin_db_ecu_properties_by_address = dll.tsdb_get_lin_db_ecu_properties_by_address
tsdb_get_lin_db_ecu_properties_by_address.argtypes = [c_char_p,PDBECUProperties]  
tsdb_get_lin_db_ecu_properties_by_address.restype = TS_ReturnType
tsdb_get_lin_db_ecu_properties_by_address.errcheck = check_status_operation

# 通过索引获取指定数据库的ECU信息
tsdb_get_lin_db_ecu_properties_by_index = dll.tsdb_get_lin_db_ecu_properties_by_index
tsdb_get_lin_db_ecu_properties_by_index.argtypes = [PDBECUProperties]  
tsdb_get_lin_db_ecu_properties_by_index.restype = TS_ReturnType
tsdb_get_lin_db_ecu_properties_by_index.errcheck = check_status_operation

# 通过地址获取指定数据库的Frame信息
tsdb_get_lin_db_frame_properties_by_address = dll.tsdb_get_lin_db_frame_properties_by_address
tsdb_get_lin_db_frame_properties_by_address.argtypes = [c_char_p,PDBFrameProperties]  
tsdb_get_lin_db_frame_properties_by_address.restype = TS_ReturnType
tsdb_get_lin_db_frame_properties_by_address.errcheck = check_status_operation

# 通过索引获取指定数据库的Frame信息
tsdb_get_lin_db_frame_properties_by_index = dll.tsdb_get_lin_db_frame_properties_by_index
tsdb_get_lin_db_frame_properties_by_index.argtypes = [PDBFrameProperties]  
tsdb_get_lin_db_frame_properties_by_index.restype = TS_ReturnType
tsdb_get_lin_db_frame_properties_by_index.errcheck = check_status_operation

# 通过数据库索引获取指定数据库的Frame信息
tsdb_get_lin_db_frame_properties_by_db_index = dll.tsdb_get_lin_db_frame_properties_by_db_index
tsdb_get_lin_db_frame_properties_by_db_index.argtypes = [s32,s32,PDBFrameProperties]  
tsdb_get_lin_db_frame_properties_by_db_index.restype = TS_ReturnType
tsdb_get_lin_db_frame_properties_by_db_index.errcheck = check_status_operation

# 通过地址获取指定数据库的Signal信息
tsdb_get_lin_db_signal_properties_by_address = dll.tsdb_get_lin_db_signal_properties_by_address
tsdb_get_lin_db_signal_properties_by_address.argtypes = [c_char_p,PDBSignalProperties]  
tsdb_get_lin_db_signal_properties_by_address.restype = TS_ReturnType
tsdb_get_lin_db_signal_properties_by_address.errcheck = check_status_operation

# 通过索引获取指定数据库的Signal信息
tsdb_get_lin_db_signal_properties_by_index = dll.tsdb_get_lin_db_signal_properties_by_index
tsdb_get_lin_db_signal_properties_by_index.argtypes = [PDBSignalProperties]  
tsdb_get_lin_db_signal_properties_by_index.restype = TS_ReturnType
tsdb_get_lin_db_signal_properties_by_index.errcheck = check_status_operation

# 通过数据库索引获取指定数据库的Signal信息
tsdb_get_lin_db_signal_properties_by_db_index = dll.tsdb_get_lin_db_signal_properties_by_db_index
tsdb_get_lin_db_signal_properties_by_db_index.argtypes = [s32,s32,PDBSignalProperties]  
tsdb_get_lin_db_signal_properties_by_db_index.restype = TS_ReturnType
tsdb_get_lin_db_signal_properties_by_db_index.errcheck = check_status_operation

# 通过Frame索引获取指定数据库的Signal信息
tsdb_get_lin_db_signal_properties_by_frame_index = dll.tsdb_get_lin_db_signal_properties_by_frame_index
tsdb_get_lin_db_signal_properties_by_frame_index.argtypes = [s32,s32,s32,PDBSignalProperties]  
tsdb_get_lin_db_signal_properties_by_frame_index.restype = TS_ReturnType
tsdb_get_lin_db_signal_properties_by_frame_index.errcheck = check_status_operation

# 获取报文中信号值
tscom_get_lin_signal_value = dll.tscom_get_lin_signal_value #函数对象
tscom_get_lin_signal_value.argtypes = [PLINSignal,pu8] #指定参数类型
tscom_get_lin_signal_value.restype = c_double 

# 设置报文中的信号值
tscom_set_lin_signal_value = dll.tscom_set_lin_signal_value #函数对象
tscom_set_lin_signal_value.argtypes = [PLINSignal,pu8,double] #指定参数类型
tscom_set_lin_signal_value.restype = TS_ReturnType 
tscom_set_lin_signal_value.errcheck = check_status_operation


# flexray API

# 启动 flexray 网络
tsflexray_start_net = dll.tsflexray_start_net
tsflexray_start_net.argtypes = [s32,s32]  
tsflexray_start_net.restype = TS_ReturnType
tsflexray_start_net.errcheck = check_status_operation

# 停止 flexray 网络
tsflexray_stop_net = dll.tsflexray_stop_net
tsflexray_stop_net.argtypes = [s32,s32]  
tsflexray_stop_net.restype = TS_ReturnType
tsflexray_stop_net.errcheck = check_status_operation

# 使能wakeup_pattern
tsflexray_wakeup_pattern = dll.tsflexray_wakeup_pattern
tsflexray_wakeup_pattern.argtypes = [s32,s32]  
tsflexray_wakeup_pattern.restype = TS_ReturnType
tsflexray_wakeup_pattern.errcheck = check_status_operation

tsflexray_set_controller_frametrigger = dll.tsflexray_set_controller_frametrigger
tsflexray_set_controller_frametrigger.argtypes = [s32,PLibFlexray_controller_config,ps32,s32,PLibTrigger_def,s32,s32]  
tsflexray_set_controller_frametrigger.restype = TS_ReturnType
tsflexray_set_controller_frametrigger.errcheck = check_status_operation

# flexray 发送
# 异步单帧发送flexray报文
tsapp_transmit_flexray_async = dll.tsapp_transmit_flexray_async
tsapp_transmit_flexray_async.argtypes = [PFlexray]  
tsapp_transmit_flexray_async.restype = TS_ReturnType
tsapp_transmit_flexray_async.errcheck = check_status_operation

# 同步单帧发送flexray报文
tsapp_transmit_flexray_sync = dll.tsapp_transmit_flexray_sync
tsapp_transmit_flexray_sync.argtypes = [PFlexray,s32]  
tsapp_transmit_flexray_sync.restype = TS_ReturnType
tsapp_transmit_flexray_sync.errcheck = check_status_operation

# flexray报文接收
# 接收flexray 报文
tsfifo_receive_flexray_msgs = dll.tsfifo_receive_flexray_msgs
tsfifo_receive_flexray_msgs.argtypes = [PFlexray,ps32,s32,s32]  
tsfifo_receive_flexray_msgs.restype = TS_ReturnType
tsfifo_receive_flexray_msgs.errcheck = check_status_operation

# 获取fifo 中flexray报文数量
tsfifo_read_flexray_buffer_frame_count = dll.tsfifo_read_flexray_buffer_frame_count
tsfifo_read_flexray_buffer_frame_count.argtypes = [s32,ps32]  
tsfifo_read_flexray_buffer_frame_count.restype = TS_ReturnType
tsfifo_read_flexray_buffer_frame_count.errcheck = check_status_operation

# 获取fifo 中TX flexray报文数量
tsfifo_read_flexray_tx_buffer_frame_count = dll.tsfifo_read_flexray_tx_buffer_frame_count
tsfifo_read_flexray_tx_buffer_frame_count.argtypes = [s32,ps32]  
tsfifo_read_flexray_tx_buffer_frame_count.restype = TS_ReturnType
tsfifo_read_flexray_tx_buffer_frame_count.errcheck = check_status_operation

# 获取fifo 中RX flexray报文数量
tsfifo_read_flexray_rx_buffer_frame_count = dll.tsfifo_read_flexray_rx_buffer_frame_count
tsfifo_read_flexray_rx_buffer_frame_count.argtypes = [s32,ps32]  
tsfifo_read_flexray_rx_buffer_frame_count.restype = TS_ReturnType
tsfifo_read_flexray_rx_buffer_frame_count.errcheck = check_status_operation

# 清空 flexray fifo
tsfifo_clear_flexray_receive_buffers = dll.tsfifo_clear_flexray_receive_buffers
tsfifo_clear_flexray_receive_buffers.argtypes = [s32]  
tsfifo_clear_flexray_receive_buffers.restype = TS_ReturnType
tsfifo_clear_flexray_receive_buffers.errcheck = check_status_operation

# flexray 回调事件
# 注册预发送事件
tsapp_register_pretx_event_flexray = dll.tsapp_register_pretx_event_flexray
tsapp_register_pretx_event_flexray.argtypes = [ps32,OnTx_RxFUNC_Flexray]  
tsapp_register_pretx_event_flexray.restype = TS_ReturnType
tsapp_register_pretx_event_flexray.errcheck = check_status_operation

# 注销预发送事件
tsapp_unregister_pretx_event_flexray = dll.tsapp_unregister_pretx_event_flexray
tsapp_unregister_pretx_event_flexray.argtypes = [ps32,OnTx_RxFUNC_Flexray]  
tsapp_unregister_pretx_event_flexray.restype = TS_ReturnType
tsapp_unregister_pretx_event_flexray.errcheck = check_status_operation

tsapp_unregister_pretx_events_flexray = dll.tsapp_unregister_pretx_events_flexray
tsapp_unregister_pretx_events_flexray.argtypes = [ps32]  
tsapp_unregister_pretx_events_flexray.restype = TS_ReturnType
tsapp_unregister_pretx_events_flexray.errcheck = check_status_operation

# 注册rx_tx事件
tsapp_register_event_flexray = dll.tsapp_register_event_flexray
tsapp_register_event_flexray.argtypes = [ps32,OnTx_RxFUNC_Flexray]  
tsapp_register_event_flexray.restype = TS_ReturnType
tsapp_register_event_flexray.errcheck = check_status_operation

# 注销rx_tx事件
tsapp_unregister_event_flexray = dll.tsapp_unregister_event_flexray
tsapp_unregister_event_flexray.argtypes = [ps32,OnTx_RxFUNC_Flexray]  
tsapp_unregister_event_flexray.restype = TS_ReturnType
tsapp_unregister_event_flexray.errcheck = check_status_operation

# flexray db info

# 载入数据库
tsdb_load_flexray_db = dll.tsdb_load_flexray_db
tsdb_load_flexray_db.argtypes = [c_char_p,c_char_p,ps32]  
tsdb_load_flexray_db.restype = TS_ReturnType
tsdb_load_flexray_db.errcheck = check_status_operation

# 卸载指定数据库
tsdb_unload_flexray_db = dll.tsdb_unload_flexray_db
tsdb_unload_flexray_db.argtypes = [s32]  
tsdb_unload_flexray_db.restype = TS_ReturnType
tsdb_unload_flexray_db.errcheck = check_status_operation

# 卸载所有数据库
tsdb_unload_flexray_dbs = dll.tsdb_unload_flexray_dbs
tsdb_unload_flexray_dbs.argtypes = []  
tsdb_unload_flexray_dbs.restype = TS_ReturnType
tsdb_unload_flexray_dbs.errcheck = check_status_operation

# get flexray cluster parameters by cluster name
tsdb_get_flexray_cluster_parameters = dll.db_get_flexray_cluster_parameters
tsdb_get_flexray_cluster_parameters.argtypes = [c_char_p,PFlexRayClusterParameters]  
tsdb_get_flexray_cluster_parameters.restype = TS_ReturnType
tsdb_get_flexray_cluster_parameters.errcheck = check_status_operation

# get flexray controller parameters by cluster name and controller name
tsdb_get_flexray_controller_parameters = dll.db_get_flexray_controller_parameters
tsdb_get_flexray_controller_parameters.argtypes = [c_char_p,PFlexRayControllerParameters]  
tsdb_get_flexray_controller_parameters.restype = TS_ReturnType
tsdb_get_flexray_controller_parameters.errcheck = check_status_operation


# 获取加载的数据库数量
tsdb_get_flexray_db_count = dll.tsdb_get_flexray_db_count
tsdb_get_flexray_db_count.argtypes = [ps32]  
tsdb_get_flexray_db_count.restype = TS_ReturnType
tsdb_get_flexray_db_count.errcheck = check_status_operation

# 通过索引获取数据库id
tsdb_get_flexray_db_id = dll.tsdb_get_flexray_db_id
tsdb_get_flexray_db_id.argtypes = [s32,ps32]  
tsdb_get_flexray_db_id.restype = TS_ReturnType
tsdb_get_flexray_db_id.errcheck = check_status_operation

# 通过地址获取指定数据库的DB信息
tsdb_get_flexray_db_properties_by_address = dll.tsdb_get_flexray_db_properties_by_address
tsdb_get_flexray_db_properties_by_address.argtypes = [c_char_p,PDBProperties]  
tsdb_get_flexray_db_properties_by_address.restype = TS_ReturnType
tsdb_get_flexray_db_properties_by_address.errcheck = check_status_operation

# 通过索引获取指定数据库的DB信息
tsdb_get_flexray_db_properties_by_index = dll.tsdb_get_flexray_db_properties_by_index
tsdb_get_flexray_db_properties_by_index.argtypes = [PDBProperties]  
tsdb_get_flexray_db_properties_by_index.restype = TS_ReturnType
tsdb_get_flexray_db_properties_by_index.errcheck = check_status_operation

# 通过地址获取指定数据库的ECU信息
tsdb_get_flexray_db_ecu_properties_by_address = dll.tsdb_get_flexray_db_ecu_properties_by_address
tsdb_get_flexray_db_ecu_properties_by_address.argtypes = [c_char_p,PDBECUProperties]  
tsdb_get_flexray_db_ecu_properties_by_address.restype = TS_ReturnType
tsdb_get_flexray_db_ecu_properties_by_address.errcheck = check_status_operation

# 通过索引获取指定数据库的ECU信息
tsdb_get_flexray_db_ecu_properties_by_index = dll.tsdb_get_flexray_db_ecu_properties_by_index
tsdb_get_flexray_db_ecu_properties_by_index.argtypes = [PDBECUProperties]  
tsdb_get_flexray_db_ecu_properties_by_index.restype = TS_ReturnType
tsdb_get_flexray_db_ecu_properties_by_index.errcheck = check_status_operation

# 通过地址获取指定数据库的Frame信息
tsdb_get_flexray_db_frame_properties_by_address = dll.tsdb_get_flexray_db_frame_properties_by_address
tsdb_get_flexray_db_frame_properties_by_address.argtypes = [c_char_p,PDBFrameProperties]  
tsdb_get_flexray_db_frame_properties_by_address.restype = TS_ReturnType
tsdb_get_flexray_db_frame_properties_by_address.errcheck = check_status_operation

# 通过索引获取指定数据库的Frame信息
tsdb_get_flexray_db_frame_properties_by_index = dll.tsdb_get_flexray_db_frame_properties_by_index
tsdb_get_flexray_db_frame_properties_by_index.argtypes = [PDBFrameProperties]  
tsdb_get_flexray_db_frame_properties_by_index.restype = TS_ReturnType
tsdb_get_flexray_db_frame_properties_by_index.errcheck = check_status_operation

# 通过数据库索引获取指定数据库的Frame信息
tsdb_get_flexray_db_frame_properties_by_db_index = dll.tsdb_get_flexray_db_frame_properties_by_db_index
tsdb_get_flexray_db_frame_properties_by_db_index.argtypes = [s32,s32,PDBFrameProperties]  
tsdb_get_flexray_db_frame_properties_by_db_index.restype = TS_ReturnType
tsdb_get_flexray_db_frame_properties_by_db_index.errcheck = check_status_operation

# 通过地址获取指定数据库的Signal信息
tsdb_get_flexray_db_signal_properties_by_address = dll.tsdb_get_flexray_db_signal_properties_by_address
tsdb_get_flexray_db_signal_properties_by_address.argtypes = [c_char_p,PDBSignalProperties]  
tsdb_get_flexray_db_signal_properties_by_address.restype = TS_ReturnType
tsdb_get_flexray_db_signal_properties_by_address.errcheck = check_status_operation

# 通过索引获取指定数据库的Signal信息
tsdb_get_flexray_db_signal_properties_by_index = dll.tsdb_get_flexray_db_signal_properties_by_index
tsdb_get_flexray_db_signal_properties_by_index.argtypes = [PDBSignalProperties]  
tsdb_get_flexray_db_signal_properties_by_index.restype = TS_ReturnType
tsdb_get_flexray_db_signal_properties_by_index.errcheck = check_status_operation

# 通过数据库索引获取指定数据库的Signal信息
tsdb_get_flexray_db_signal_properties_by_db_index = dll.tsdb_get_flexray_db_signal_properties_by_db_index
tsdb_get_flexray_db_signal_properties_by_db_index.argtypes = [s32,s32,PDBSignalProperties]  
tsdb_get_flexray_db_signal_properties_by_db_index.restype = TS_ReturnType
tsdb_get_flexray_db_signal_properties_by_db_index.errcheck = check_status_operation

# 通过Frame索引获取指定数据库的Signal信息
tsdb_get_flexray_db_signal_properties_by_frame_index = dll.tsdb_get_flexray_db_signal_properties_by_frame_index
tsdb_get_flexray_db_signal_properties_by_frame_index.argtypes = [s32,s32,s32,PDBSignalProperties]  
tsdb_get_flexray_db_signal_properties_by_frame_index.restype = TS_ReturnType
tsdb_get_flexray_db_signal_properties_by_frame_index.errcheck = check_status_operation


tscom_flexray_get_signal_definition = dll.tscom_flexray_get_signal_definition
tscom_flexray_get_signal_definition.argtypes = [c_char_p,PFlexRaySignal]  
tscom_flexray_get_signal_definition.restype = TS_ReturnType
tscom_flexray_get_signal_definition.errcheck = check_status_operation

flexray_rbs_update_frame_by_header = dll.flexray_rbs_update_frame_by_header
flexray_rbs_update_frame_by_header.argtypes = [PFlexray]  
flexray_rbs_update_frame_by_header.restype = TS_ReturnType


# 获取报文中信号值
tscom_get_flexray_signal_value = dll.tscom_get_flexray_signal_value #函数对象
tscom_get_flexray_signal_value.argtypes = [PFlexRaySignal,pu8] #指定参数类型
tscom_get_flexray_signal_value.restype = c_double 

#获取报文原始值
get_flexray_signal_raw_value = dll.get_flexray_signal_raw_value #函数对象
get_flexray_signal_raw_value.argtypes = [PFlexRaySignal,pu8] #指定参数类型
get_flexray_signal_raw_value.restype = s64 

# 设置报文中的信号值
tscom_set_flexray_signal_value = dll.tscom_set_flexray_signal_value #函数对象
tscom_set_flexray_signal_value.argtypes = [PFlexRaySignal,pu8,double] #指定参数类型
tscom_set_flexray_signal_value.restype = TS_ReturnType 
tscom_set_flexray_signal_value.errcheck = check_status_operation

# RBS 

# CAN RBS

# 开启rbs
tscom_can_rbs_start = dll.tscom_can_rbs_start
tscom_can_rbs_start.argtypes = []  
tscom_can_rbs_start.restype = TS_ReturnType
tscom_can_rbs_start.errcheck = check_status_operation

# 停止rbs
tscom_can_rbs_stop = dll.tscom_can_rbs_stop
tscom_can_rbs_stop.argtypes = []  
tscom_can_rbs_stop.restype = TS_ReturnType
tscom_can_rbs_stop.errcheck = check_status_operation

# rbs是否启动
tscom_can_rbs_is_running = dll.tscom_can_rbs_is_running
tscom_can_rbs_is_running.argtypes = [POINTER(c_bool)]  
tscom_can_rbs_is_running.restype = TS_ReturnType
tscom_can_rbs_is_running.errcheck = check_status_operation

# RBS 配置
tscom_can_rbs_configure = dll.tscom_can_rbs_configure
tscom_can_rbs_configure.argtypes = [c_bool,c_bool,c_bool,s32]  
tscom_can_rbs_configure.restype = TS_ReturnType
tscom_can_rbs_configure.errcheck = check_status_operation

# 通过 network name 激活 network 是否包括子节点
tscom_can_rbs_activate_network_by_name = dll.tscom_can_rbs_activate_network_by_name
tscom_can_rbs_activate_network_by_name.argtypes = [s32,c_bool,c_char_p,c_bool]  
tscom_can_rbs_activate_network_by_name.restype = TS_ReturnType
tscom_can_rbs_activate_network_by_name.errcheck = check_status_operation

# 通过 node name 激活 node  是否包括子节点
tscom_can_rbs_activate_node_by_name = dll.tscom_can_rbs_activate_node_by_name
tscom_can_rbs_activate_node_by_name.argtypes = [s32,c_bool,c_char_p,c_char_p,c_bool]  
tscom_can_rbs_activate_node_by_name.restype = TS_ReturnType
tscom_can_rbs_activate_node_by_name.errcheck = check_status_operation

# 通过 message name 激活 message 
tscom_can_rbs_activate_message_by_name = dll.tscom_can_rbs_activate_message_by_name
tscom_can_rbs_activate_message_by_name.argtypes = [s32,c_bool,c_char_p,c_char_p,c_char_p]  
tscom_can_rbs_activate_message_by_name.restype = TS_ReturnType
tscom_can_rbs_activate_message_by_name.errcheck = check_status_operation

# 激活所有network rbs
tscom_can_rbs_activate_all_networks = dll.tscom_can_rbs_activate_all_networks
tscom_can_rbs_activate_all_networks.argtypes = [c_bool,c_bool]  
tscom_can_rbs_activate_all_networks.restype = TS_ReturnType
tscom_can_rbs_activate_all_networks.errcheck = check_status_operation

# 通过信号地址获取信号值
tscom_can_rbs_get_signal_value_by_address = dll.tscom_can_rbs_get_signal_value_by_address
tscom_can_rbs_get_signal_value_by_address.argtypes = [c_char_p,pdouble]  
tscom_can_rbs_get_signal_value_by_address.restype = TS_ReturnType
tscom_can_rbs_get_signal_value_by_address.errcheck = check_status_operation

# 通过信号元素获取信号值
tscom_can_rbs_get_signal_value_by_element = dll.tscom_can_rbs_get_signal_value_by_element
tscom_can_rbs_get_signal_value_by_element.argtypes = [s32,c_char_p,c_char_p,c_char_p,c_char_p,pdouble]  
tscom_can_rbs_get_signal_value_by_element.restype = TS_ReturnType
tscom_can_rbs_get_signal_value_by_element.errcheck = check_status_operation

# 通过信号地址设置信号值
tscom_can_rbs_set_signal_value_by_address = dll.tscom_can_rbs_set_signal_value_by_address
tscom_can_rbs_set_signal_value_by_address.argtypes = [c_char_p,double]  
tscom_can_rbs_set_signal_value_by_address.restype = TS_ReturnType
tscom_can_rbs_set_signal_value_by_address.errcheck = check_status_operation

# 通过信号元素设置信号值
tscom_can_rbs_set_signal_value_by_element = dll.tscom_can_rbs_set_signal_value_by_element
tscom_can_rbs_set_signal_value_by_element.argtypes = [s32,c_char_p,c_char_p,c_char_p,c_char_p,double]  
tscom_can_rbs_set_signal_value_by_element.restype = TS_ReturnType
tscom_can_rbs_set_signal_value_by_element.errcheck = check_status_operation

# 设置rbs 报文周期
tscom_can_rbs_set_message_cycle_by_name = dll.tscom_can_rbs_set_message_cycle_by_name
tscom_can_rbs_set_message_cycle_by_name.argtypes = [c_float,c_char_p,c_char_p,c_char_p]  
tscom_can_rbs_set_message_cycle_by_name.restype = TS_ReturnType
tscom_can_rbs_set_message_cycle_by_name.errcheck = check_status_operation

# lin RBS

# 开启rbs
tscom_lin_rbs_start = dll.tscom_lin_rbs_start
tscom_lin_rbs_start.argtypes = []  
tscom_lin_rbs_start.restype = TS_ReturnType
tscom_lin_rbs_start.errcheck = check_status_operation

# 停止rbs
tscom_lin_rbs_stop = dll.tscom_lin_rbs_stop
tscom_lin_rbs_stop.argtypes = []  
tscom_lin_rbs_stop.restype = TS_ReturnType
tscom_lin_rbs_stop.errcheck = check_status_operation

# rbs是否启动
tscom_lin_rbs_is_running = dll.tscom_lin_rbs_is_running
tscom_lin_rbs_is_running.argtypes = [POINTER(c_bool)]  
tscom_lin_rbs_is_running.restype = TS_ReturnType
tscom_lin_rbs_is_running.errcheck = check_status_operation

# RBS 配置
tscom_lin_rbs_configure = dll.tscom_lin_rbs_configure
tscom_lin_rbs_configure.argtypes = [c_bool,c_bool,c_bool,s32]  
tscom_lin_rbs_configure.restype = TS_ReturnType
tscom_lin_rbs_configure.errcheck = check_status_operation

# 通过 network name 激活 network 是否包括子节点
tscom_lin_rbs_activate_network_by_name = dll.tscom_lin_rbs_activate_network_by_name
tscom_lin_rbs_activate_network_by_name.argtypes = [s32,c_bool,c_char_p,c_bool]  
tscom_lin_rbs_activate_network_by_name.restype = TS_ReturnType
tscom_lin_rbs_activate_network_by_name.errcheck = check_status_operation

# 通过 node name 激活 node  是否包括子节点
tscom_lin_rbs_activate_node_by_name = dll.tscom_lin_rbs_activate_node_by_name
tscom_lin_rbs_activate_node_by_name.argtypes = [s32,c_bool,c_char_p,c_char_p,c_bool]  
tscom_lin_rbs_activate_node_by_name.restype = TS_ReturnType
tscom_lin_rbs_activate_node_by_name.errcheck = check_status_operation

# 通过 message name 激活 message 
tscom_lin_rbs_activate_message_by_name = dll.tscom_lin_rbs_activate_message_by_name
tscom_lin_rbs_activate_message_by_name.argtypes = [s32,c_bool,c_char_p,c_char_p,c_char_p]  
tscom_lin_rbs_activate_message_by_name.restype = TS_ReturnType
tscom_lin_rbs_activate_message_by_name.errcheck = check_status_operation

# 激活所有network rbs
tscom_lin_rbs_activate_all_networks = dll.tscom_lin_rbs_activate_all_networks
tscom_lin_rbs_activate_all_networks.argtypes = [c_bool,c_bool]  
tscom_lin_rbs_activate_all_networks.restype = TS_ReturnType
tscom_lin_rbs_activate_all_networks.errcheck = check_status_operation

# 通过信号地址获取信号值
tscom_lin_rbs_get_signal_value_by_address = dll.tscom_lin_rbs_get_signal_value_by_address
tscom_lin_rbs_get_signal_value_by_address.argtypes = [c_char_p,pdouble]  
tscom_lin_rbs_get_signal_value_by_address.restype = TS_ReturnType
tscom_lin_rbs_get_signal_value_by_address.errcheck = check_status_operation

# 通过信号元素获取信号值
tscom_lin_rbs_get_signal_value_by_element = dll.tscom_lin_rbs_get_signal_value_by_element
tscom_lin_rbs_get_signal_value_by_element.argtypes = [s32,c_char_p,c_char_p,c_char_p,c_char_p,pdouble]  
tscom_lin_rbs_get_signal_value_by_element.restype = TS_ReturnType
tscom_lin_rbs_get_signal_value_by_element.errcheck = check_status_operation

# 通过信号地址设置信号值
tscom_lin_rbs_set_signal_value_by_address = dll.tscom_lin_rbs_set_signal_value_by_address
tscom_lin_rbs_set_signal_value_by_address.argtypes = [c_char_p,double]  
tscom_lin_rbs_set_signal_value_by_address.restype = TS_ReturnType
tscom_lin_rbs_set_signal_value_by_address.errcheck = check_status_operation

# 通过信号元素设置信号值
tscom_lin_rbs_set_signal_value_by_element = dll.tscom_lin_rbs_set_signal_value_by_element
tscom_lin_rbs_set_signal_value_by_element.argtypes = [s32,c_char_p,c_char_p,c_char_p,c_char_p,double]  
tscom_lin_rbs_set_signal_value_by_element.restype = TS_ReturnType
tscom_lin_rbs_set_signal_value_by_element.errcheck = check_status_operation

# 重新加载设置
tscom_lin_rbs_reload_settings = dll.tscom_lin_rbs_reload_settings
tscom_lin_rbs_reload_settings.argtypes = []  
tscom_lin_rbs_reload_settings.restype = TS_ReturnType
tscom_lin_rbs_reload_settings.errcheck = check_status_operation

# 设置lin报文延时时间
tscom_lin_rbs_set_message_delay_time_by_name = dll.tscom_lin_rbs_set_message_delay_time_by_name
tscom_lin_rbs_set_message_delay_time_by_name.argtypes = [s32,s32,c_char_p,c_char_p,c_char_p]  
tscom_lin_rbs_set_message_delay_time_by_name.restype = TS_ReturnType
tscom_lin_rbs_set_message_delay_time_by_name.errcheck = check_status_operation




# flexray RBS

# 使能/失能flexray rbs功能
tscom_flexray_rbs_enable = dll.tscom_flexray_rbs_enable
tscom_flexray_rbs_enable.argtypes = [c_bool]  
tscom_flexray_rbs_enable.restype = TS_ReturnType
tscom_flexray_rbs_enable.errcheck = check_status_operation

# 开启rbs
tscom_flexray_rbs_start = dll.tscom_flexray_rbs_start
tscom_flexray_rbs_start.argtypes = []  
tscom_flexray_rbs_start.restype = TS_ReturnType
tscom_flexray_rbs_start.errcheck = check_status_operation

# 停止rbs
tscom_flexray_rbs_stop = dll.tscom_flexray_rbs_stop
tscom_flexray_rbs_stop.argtypes = []  
tscom_flexray_rbs_stop.restype = TS_ReturnType
tscom_flexray_rbs_stop.errcheck = check_status_operation

# rbs是否启动
tscom_flexray_rbs_is_running = dll.tscom_flexray_rbs_is_running
tscom_flexray_rbs_is_running.argtypes = [POINTER(c_bool)]  
tscom_flexray_rbs_is_running.restype = TS_ReturnType
tscom_flexray_rbs_is_running.errcheck = check_status_operation

# RBS 配置
tscom_flexray_rbs_configure = dll.tscom_flexray_rbs_configure
tscom_flexray_rbs_configure.argtypes = [c_bool,c_bool,c_bool,s32]  
tscom_flexray_rbs_configure.restype = TS_ReturnType
tscom_flexray_rbs_configure.errcheck = check_status_operation

# 通过 network name 激活 network 是否包括子节点
tscom_flexray_rbs_activate_cluster_by_name = dll.tscom_flexray_rbs_activate_cluster_by_name
tscom_flexray_rbs_activate_cluster_by_name.argtypes = [s32,c_bool,c_char_p,c_bool]  
tscom_flexray_rbs_activate_cluster_by_name.restype = TS_ReturnType
tscom_flexray_rbs_activate_cluster_by_name.errcheck = check_status_operation

# 通过 node name 激活 node  是否包括子节点
tscom_flexray_rbs_activate_ecu_by_name = dll.tscom_flexray_rbs_activate_ecu_by_name
tscom_flexray_rbs_activate_ecu_by_name.argtypes = [s32,c_bool,c_char_p,c_char_p,c_bool]  
tscom_flexray_rbs_activate_ecu_by_name.restype = TS_ReturnType
tscom_flexray_rbs_activate_ecu_by_name.errcheck = check_status_operation

# 通过 message name 激活 message 
tscom_flexray_rbs_activate_frame_by_name = dll.tscom_flexray_rbs_activate_frame_by_name
tscom_flexray_rbs_activate_frame_by_name.argtypes = [s32,c_bool,c_char_p,c_char_p,c_char_p]  
tscom_flexray_rbs_activate_frame_by_name.restype = TS_ReturnType
tscom_flexray_rbs_activate_frame_by_name.errcheck = check_status_operation

# 激活所有network rbs
tscom_flexray_rbs_activate_all_clusters = dll.tscom_flexray_rbs_activate_all_clusters
tscom_flexray_rbs_activate_all_clusters.argtypes = [c_bool,c_bool]  
tscom_flexray_rbs_activate_all_clusters.restype = TS_ReturnType
tscom_flexray_rbs_activate_all_clusters.errcheck = check_status_operation

# 通过信号地址获取信号值
tscom_flexray_rbs_get_signal_value_by_address = dll.tscom_flexray_rbs_get_signal_value_by_address
tscom_flexray_rbs_get_signal_value_by_address.argtypes = [c_char_p,pdouble]  
tscom_flexray_rbs_get_signal_value_by_address.restype = TS_ReturnType
tscom_flexray_rbs_get_signal_value_by_address.errcheck = check_status_operation

# 通过信号元素获取信号值
tscom_flexray_rbs_get_signal_value_by_element = dll.tscom_flexray_rbs_get_signal_value_by_element
tscom_flexray_rbs_get_signal_value_by_element.argtypes = [s32,c_char_p,c_char_p,c_char_p,c_char_p,pdouble]  
tscom_flexray_rbs_get_signal_value_by_element.restype = TS_ReturnType
tscom_flexray_rbs_get_signal_value_by_element.errcheck = check_status_operation

# 通过信号地址设置信号值
tscom_flexray_rbs_set_signal_value_by_address = dll.tscom_flexray_rbs_set_signal_value_by_address
tscom_flexray_rbs_set_signal_value_by_address.argtypes = [c_char_p,double]  
tscom_flexray_rbs_set_signal_value_by_address.restype = TS_ReturnType
tscom_flexray_rbs_set_signal_value_by_address.errcheck = check_status_operation

# 通过信号元素设置信号值
tscom_flexray_rbs_set_signal_value_by_element = dll.tscom_flexray_rbs_set_signal_value_by_element
tscom_flexray_rbs_set_signal_value_by_element.argtypes = [s32,c_char_p,c_char_p,c_char_p,c_char_p,double]  
tscom_flexray_rbs_set_signal_value_by_element.restype = TS_ReturnType
tscom_flexray_rbs_set_signal_value_by_element.errcheck = check_status_operation

# 开始批量修改信号
tscom_flexray_rbs_batch_set_start = dll.tscom_flexray_rbs_batch_set_start
tscom_flexray_rbs_batch_set_start.argtypes = []  
tscom_flexray_rbs_batch_set_start.restype = TS_ReturnType
tscom_flexray_rbs_batch_set_start.errcheck = check_status_operation

# 结束批量修改信号 
tscom_flexray_rbs_batch_set_end = dll.tscom_flexray_rbs_batch_set_end
tscom_flexray_rbs_batch_set_end.argtypes = []  
tscom_flexray_rbs_batch_set_end.restype = TS_ReturnType
tscom_flexray_rbs_batch_set_end.errcheck = check_status_operation

# 设置信号值 
tscom_flexray_rbs_batch_set_signal = dll.tscom_flexray_rbs_batch_set_signal
tscom_flexray_rbs_batch_set_signal.argtypes = [c_char_p,double]  
tscom_flexray_rbs_batch_set_signal.restype = TS_ReturnType
tscom_flexray_rbs_batch_set_signal.errcheck = check_status_operation

# 设置信号为normal信号 
tscom_flexray_rbs_set_normal_signal = dll.tscom_flexray_rbs_set_normal_signal
tscom_flexray_rbs_set_normal_signal.argtypes = [c_char_p]  
tscom_flexray_rbs_set_normal_signal.restype = TS_ReturnType
tscom_flexray_rbs_set_normal_signal.errcheck = check_status_operation

# 设置信号为RC信号 
tscom_flexray_rbs_set_rc_signal = dll.tscom_flexray_rbs_set_rc_signal
tscom_flexray_rbs_set_rc_signal.argtypes = [c_char_p]  
tscom_flexray_rbs_set_rc_signal.restype = TS_ReturnType
tscom_flexray_rbs_set_rc_signal.errcheck = check_status_operation

# 设置rc信号值的限定范围 
tscom_flexray_rbs_set_rc_signal_with_limit = dll.tscom_flexray_rbs_set_rc_signal_with_limit
tscom_flexray_rbs_set_rc_signal_with_limit.argtypes = [c_char_p,s32,s32]  
tscom_flexray_rbs_set_rc_signal_with_limit.restype = TS_ReturnType
tscom_flexray_rbs_set_rc_signal_with_limit.errcheck = check_status_operation

# 设置信号为crc信号 
tscom_flexray_rbs_set_crc_signal = dll.tscom_flexray_rbs_set_crc_signal
tscom_flexray_rbs_set_crc_signal.argtypes = [c_char_p,c_char_p,s32,s32]  
tscom_flexray_rbs_set_crc_signal.restype = TS_ReturnType
tscom_flexray_rbs_set_crc_signal.errcheck = check_status_operation


# ONLINE REPLAY

# 添加在线回放配置
tslog_add_online_replay_config = dll.tslog_add_online_replay_config
tslog_add_online_replay_config.argtypes = [c_char_p,ps32]  
tslog_add_online_replay_config.restype = TS_ReturnType
tslog_add_online_replay_config.errcheck = check_status_operation

# 设置在线回放配置
tslog_set_online_replay_config = dll.tslog_set_online_replay_config
tslog_set_online_replay_config.argtypes = [s32,c_char_p,c_char_p,c_bool,c_bool,s32,s32,c_bool,c_bool,c_char_p]  
tslog_set_online_replay_config.restype = TS_ReturnType
tslog_set_online_replay_config.errcheck = check_status_operation

# 获取在线回放配置
tslog_get_online_replay_config = dll.tslog_get_online_replay_config
tslog_get_online_replay_config.argtypes = [s32,charpp,charpp,POINTER(c_bool),POINTER(c_bool),ps32,ps32,POINTER(c_bool),POINTER(c_bool),charpp]  
tslog_get_online_replay_config.restype = TS_ReturnType
tslog_get_online_replay_config.errcheck = check_status_operation

# 获取在线回放文件数量
tslog_get_online_replay_count = dll.tslog_get_online_replay_count
tslog_get_online_replay_count.argtypes = [ps32]
tslog_set_online_replay_config.restype = TS_ReturnType
tslog_get_online_replay_count.errcheck = check_status_operation

# 删除在线回放配置
tslog_del_online_replay_config = dll.tslog_del_online_replay_config
tslog_del_online_replay_config.argtypes = [s32]
tslog_del_online_replay_config.restype = TS_ReturnType
tslog_del_online_replay_config.errcheck = check_status_operation

# 删除所有在线回放配置
tslog_del_online_replay_configs = dll.tslog_del_online_replay_configs
tslog_del_online_replay_configs.argtypes = []
tslog_del_online_replay_configs.restype = TS_ReturnType
tslog_del_online_replay_configs.errcheck = check_status_operation

# 开始在线回放
tslog_start_online_replay = dll.tslog_start_online_replay
tslog_start_online_replay.argtypes = [s32]
tslog_start_online_replay.restype = TS_ReturnType
tslog_start_online_replay.errcheck = check_status_operation

# 所有文件开始回放
tslog_start_online_replays = dll.tslog_start_online_replays
tslog_start_online_replays.argtypes = []
tslog_start_online_replays.restype = TS_ReturnType
tslog_start_online_replays.errcheck = check_status_operation

# 暂停在线回放
tslog_pause_online_replay = dll.tslog_pause_online_replay
tslog_pause_online_replay.argtypes = [s32]
tslog_pause_online_replay.restype = TS_ReturnType
tslog_pause_online_replay.errcheck = check_status_operation

# 所有文件暂停回放
tslog_pause_online_replays = dll.tslog_pause_online_replays
tslog_pause_online_replays.argtypes = []
tslog_pause_online_replays.restype = TS_ReturnType
tslog_pause_online_replays.errcheck = check_status_operation

# 停止在线回放
tslog_stop_online_replay = dll.tslog_stop_online_replay
tslog_stop_online_replay.argtypes = [s32]
tslog_stop_online_replay.restype = TS_ReturnType
tslog_stop_online_replay.errcheck = check_status_operation

# 所有文件停止在线回放
tslog_stop_online_replays = dll.tslog_stop_online_replays
tslog_stop_online_replays.argtypes = []
tslog_stop_online_replays.restype = TS_ReturnType
tslog_stop_online_replays.errcheck = check_status_operation

# 获取在线回放状态
tslog_get_online_replay_status = dll.tslog_get_online_replay_status
tslog_get_online_replay_status.argtypes = [s32,ps32,POINTER(c_float)]
tslog_get_online_replay_status.restype = TS_ReturnType
tslog_get_online_replay_status.errcheck = check_status_operation

# BLF 文件处理

# 读操作
# 开始读取blf
tslog_blf_read_start = dll.tslog_blf_read_start
tslog_blf_read_start.argtypes = [c_char_p, ps32, s32]
tslog_blf_read_start.restype = TS_ReturnType
tslog_blf_read_start.errcheck = check_status_operation

# 逐个读取blf 内容
tslog_blf_read_object = dll.tslog_blf_read_object
tslog_blf_read_start.argtypes = [s32, ps32, ps32,PCAN,PLIN,PCANFD]
tslog_blf_read_start.restype = TS_ReturnType
tslog_blf_read_start.errcheck = check_status_operation

# 结束读取blf
tslog_blf_read_end = dll.tslog_blf_read_end
tslog_blf_read_end.argtypes = [s32]
tslog_blf_read_end.restype = TS_ReturnType
tslog_blf_read_end.errcheck = check_status_operation

# 写操作

# 开始写入blf
tslog_blf_write_start = dll.tslog_blf_write_start
tslog_blf_write_start.argtypes = [c_char_p, ps32]
tslog_blf_write_start.restype = TS_ReturnType
tslog_blf_write_start.errcheck = check_status_operation

# 写入 can 数据
tslog_blf_write_can = dll.tslog_blf_write_can
tslog_blf_write_can.argtypes = [s32, PCAN]
tslog_blf_write_can.restype = TS_ReturnType
tslog_blf_write_can.errcheck = check_status_operation

# 写入 canfd 数据
tslog_blf_write_can_fd = dll.tslog_blf_write_can_fd
tslog_blf_write_can_fd.argtypes = [s32, PCANFD]
tslog_blf_write_can_fd.restype = TS_ReturnType
tslog_blf_write_can_fd.errcheck = check_status_operation

# 写入 lin 数据
tslog_blf_write_lin = dll.tslog_blf_write_lin
tslog_blf_write_lin.argtypes = [s32, PLIN]
tslog_blf_write_lin.restype = TS_ReturnType
tslog_blf_write_lin.errcheck = check_status_operation

# 结束写入blf
tslog_blf_write_end = dll.tslog_blf_write_end
tslog_blf_write_end.argtypes = [s32]
tslog_blf_write_end.restype = TS_ReturnType
tslog_blf_write_end.errcheck = check_status_operation

# UDS诊断

# CAN
# 创建诊断服务
tsdiag_can_create = dll.tsdiag_can_create
tsdiag_can_create.argtypes = [pu8,s32,u8,u8,s32,c_bool,s32,c_bool,s32,c_bool]
tsdiag_can_create.restype = TS_ReturnType
tsdiag_can_create.errcheck = check_status_operation

# 删除指定诊断服务
tsdiag_can_delete = dll.tsdiag_can_delete
tsdiag_can_delete.argtypes = [u8]
tsdiag_can_delete.restype = TS_ReturnType
tsdiag_can_delete.errcheck = check_status_operation

# 删除所有诊断服务
tsdiag_can_delete_all = dll.tsdiag_can_delete_all
tsdiag_can_delete_all.argtypes = []
tsdiag_can_delete_all.restype = TS_ReturnType
tsdiag_can_delete_all.errcheck = check_status_operation

# 设置p2 扩展时间
tsdiag_set_p2_extended = dll.tsdiag_set_p2_extended
tsdiag_set_p2_extended.argtypes = [u8,s32]
tsdiag_set_p2_extended.restype = TS_ReturnType
tsdiag_set_p2_extended.errcheck = check_status_operation

# 设置p2 超时时间
tsdiag_set_p2_timeout = dll.tsdiag_set_p2_extended
tsdiag_set_p2_timeout.argtypes = [u8,s32]
tsdiag_set_p2_timeout.restype = TS_ReturnType
tsdiag_set_p2_timeout.errcheck = check_status_operation

# 设置p3 服务器时间
tsdiag_set_s3_servertime = dll.tsdiag_set_s3_servertime
tsdiag_set_s3_servertime.argtypes = [u8,s32]
tsdiag_set_s3_servertime.restype = TS_ReturnType
tsdiag_set_s3_servertime.errcheck = check_status_operation

# 设置p3 客户端时间
tsdiag_set_s3_clienttime = dll.tsdiag_set_s3_clienttime
tsdiag_set_s3_clienttime.argtypes = [u8,s32]
tsdiag_set_s3_clienttime.restype = TS_ReturnType
tsdiag_set_s3_clienttime.errcheck = check_status_operation

# 功能寻址 请求
tstp_can_send_functional = dll.tstp_can_send_functional
tstp_can_send_functional.argtypes = [u8,pu8,s32]
tstp_can_send_functional.restype = TS_ReturnType
tstp_can_send_functional.errcheck = check_status_operation

# 请求id 发送数据
tstp_can_send_request = dll.tstp_can_send_request
tstp_can_send_request.argtypes = [u8,pu8,s32]
tstp_can_send_request.restype = TS_ReturnType
tstp_can_send_request.errcheck = check_status_operation

# 请求并接收数据
tstp_can_request_and_get_response = dll.tstp_can_request_and_get_response
tstp_can_request_and_get_response.argtypes = [u8,pu8,s32,pu8,ps32]
tstp_can_request_and_get_response.restype = TS_ReturnType
tstp_can_request_and_get_response.errcheck = check_status_operation

# 相关诊断服务
# 10 服务
tsdiag_can_session_control = dll.tsdiag_can_session_control
tsdiag_can_session_control.argtypes = [u8,u8]
tsdiag_can_session_control.restype = TS_ReturnType
tsdiag_can_session_control.errcheck = check_status_operation

# 31
tsdiag_can_routine_control = dll.tsdiag_can_routine_control
tsdiag_can_routine_control.argtypes = [u8,u8,u16]
tsdiag_can_routine_control.restype = TS_ReturnType
tsdiag_can_routine_control.errcheck = check_status_operation

# 28
tsdiag_can_communication_control = dll.tsdiag_can_communication_control
tsdiag_can_communication_control.argtypes = [u8,u8]
tsdiag_can_communication_control.restype = TS_ReturnType
tsdiag_can_communication_control.errcheck = check_status_operation

# 27 get seed
tsdiag_can_security_access_request_seed = dll.tsdiag_can_security_access_request_seed
tsdiag_can_security_access_request_seed.argtypes = [u8,s32,pu8,ps32]
tsdiag_can_security_access_request_seed.restype = TS_ReturnType
tsdiag_can_security_access_request_seed.errcheck = check_status_operation

# 27 send key
tsdiag_can_security_access_send_key = dll.tsdiag_can_security_access_send_key
tsdiag_can_security_access_send_key.argtypes = [u8,s32,pu8,ps32]
tsdiag_can_security_access_send_key.restype = TS_ReturnType
tsdiag_can_security_access_send_key.errcheck = check_status_operation

# 34
tsdiag_can_request_download = dll.tsdiag_can_request_download
tsdiag_can_request_download.argtypes = [u8,u32,u32]
tsdiag_can_request_download.restype = TS_ReturnType
tsdiag_can_request_download.errcheck = check_status_operation

# 35
tsdiag_can_request_upload = dll.tsdiag_can_request_upload
tsdiag_can_request_upload.argtypes = [u8,u32,u32]
tsdiag_can_request_upload.restype = TS_ReturnType
tsdiag_can_request_upload.errcheck = check_status_operation

# 36
tsdiag_can_transfer_data = dll.tsdiag_can_transfer_data
tsdiag_can_transfer_data.argtypes = [u8,pu8,u32,u32]
tsdiag_can_transfer_data.restype = TS_ReturnType
tsdiag_can_transfer_data.errcheck = check_status_operation

# 37
tsdiag_can_request_transfer_exit = dll.tsdiag_can_request_transfer_exit
tsdiag_can_request_transfer_exit.argtypes = [u8]
tsdiag_can_request_transfer_exit.restype = TS_ReturnType
tsdiag_can_request_transfer_exit.errcheck = check_status_operation

# 2E
tsdiag_can_write_data_by_identifier = dll.tsdiag_can_write_data_by_identifier
tsdiag_can_write_data_by_identifier.argtypes = [u8,u16,pu8,u32]
tsdiag_can_write_data_by_identifier.restype = TS_ReturnType
tsdiag_can_write_data_by_identifier.errcheck = check_status_operation

# 22
tsdiag_can_read_data_by_identifier = dll.tsdiag_can_read_data_by_identifier
tsdiag_can_read_data_by_identifier.argtypes = [u8,u16,pu8,ps32]
tsdiag_can_read_data_by_identifier.restype = TS_ReturnType
tsdiag_can_read_data_by_identifier.errcheck = check_status_operation

# LIN 诊断
# 诊断请求
tstp_lin_master_request = dll.tstp_lin_master_request
tstp_lin_master_request.argtypes = [s32,u8,pu8,s32,s32]
tstp_lin_master_request.restype = TS_ReturnType
tstp_lin_master_request.errcheck = check_status_operation
# 
tstp_lin_master_request_intervalms = dll.tstp_lin_master_request_intervalms
tstp_lin_master_request_intervalms.argtypes = [s32,u16]
tstp_lin_master_request_intervalms.restype = TS_ReturnType
tstp_lin_master_request_intervalms.errcheck = check_status_operation
# 重启
tstp_lin_reset = dll.tstp_lin_reset
tstp_lin_reset.argtypes = [s32]
tstp_lin_reset.restype = TS_ReturnType
tstp_lin_reset.errcheck = check_status_operation

# 从节点响应
tstp_lin_slave_response_intervalms = dll.tstp_lin_slave_response_intervalms
tstp_lin_slave_response_intervalms.argtypes = [s32,u16]
tstp_lin_slave_response_intervalms.restype = TS_ReturnType
tstp_lin_slave_response_intervalms.errcheck = check_status_operation

# 22
tsdiag_lin_read_data_by_identifier = dll.tsdiag_lin_read_data_by_identifier
tsdiag_lin_read_data_by_identifier.argtypes = [s32,u8,u16,pu8,pu8,ps32,s32]
tsdiag_lin_read_data_by_identifier.restype = TS_ReturnType
tsdiag_lin_read_data_by_identifier.errcheck = check_status_operation

# 2E
tsdiag_lin_write_data_by_identifier = dll.tsdiag_lin_write_data_by_identifier
tsdiag_lin_write_data_by_identifier.argtypes = [s32,u8,u16,pu8,s32,pu8,pu8,ps32,s32]
tsdiag_lin_write_data_by_identifier.restype = TS_ReturnType
tsdiag_lin_write_data_by_identifier.errcheck = check_status_operation

# 10
tsdiag_lin_session_control = dll.tsdiag_lin_session_control
tsdiag_lin_session_control.argtypes = [s32,u8,u8,s32]
tsdiag_lin_session_control.restype = TS_ReturnType
tsdiag_lin_session_control.errcheck = check_status_operation

# 
tsdiag_lin_fault_memory_clear = dll.tsdiag_lin_fault_memory_clear
tsdiag_lin_fault_memory_clear.argtypes = [s32,u8,u8,s32]
tsdiag_lin_fault_memory_clear.restype = TS_ReturnType
tsdiag_lin_fault_memory_clear.errcheck = check_status_operation

# 
tsdiag_lin_fault_memory_read = dll.tsdiag_lin_fault_memory_read
tsdiag_lin_fault_memory_read.argtypes = [s32,u8,u8,s32]
tsdiag_lin_fault_memory_read.restype = TS_ReturnType
tsdiag_lin_fault_memory_read.errcheck = check_status_operation

# lin schedule function
tslin_batch_set_schedule_start = dll.tslin_batch_set_schedule_start
tslin_batch_set_schedule_start.argtypes = [s32]
tslin_batch_set_schedule_start.restype = TS_ReturnType
tslin_batch_set_schedule_start.errcheck = check_status_operation

tslin_batch_set_schedule_end = dll.tslin_batch_set_schedule_end
tslin_batch_set_schedule_end.argtypes = [s32]
tslin_batch_set_schedule_end.restype = TS_ReturnType
tslin_batch_set_schedule_end.errcheck = check_status_operation

tslin_batch_add_schedule_frame = dll.tslin_batch_add_schedule_frame
tslin_batch_add_schedule_frame.argtypes = [s32,PLIN,u8]
tslin_batch_add_schedule_frame.restype = TS_ReturnType
tslin_batch_add_schedule_frame.errcheck = check_status_operation

tslin_clear_schedule_tables = dll.tslin_clear_schedule_tables
tslin_clear_schedule_tables.argtypes = [s32]
tslin_clear_schedule_tables.restype = TS_ReturnType
tslin_clear_schedule_tables.errcheck = check_status_operation

tslin_switch_runtime_schedule_table = dll.tslin_switch_runtime_schedule_table
tslin_switch_runtime_schedule_table.argtypes = [s32]
tslin_switch_runtime_schedule_table.restype = TS_ReturnType
tslin_switch_runtime_schedule_table.errcheck = check_status_operation

tslin_switch_idle_schedule_table = dll.tslin_switch_idle_schedule_table
tslin_switch_idle_schedule_table.argtypes = [s32]
tslin_switch_idle_schedule_table.restype = TS_ReturnType
tslin_switch_idle_schedule_table.errcheck = check_status_operation

tslin_switch_normal_schedule_table = dll.tslin_switch_normal_schedule_table
tslin_switch_normal_schedule_table.argtypes = [s32,s32]
tslin_switch_normal_schedule_table.restype = TS_ReturnType
tslin_switch_normal_schedule_table.errcheck = check_status_operation

tslin_start_lin_channel = dll.tslin_start_lin_channel
tslin_start_lin_channel.argtypes = [s32]
tslin_start_lin_channel.restype = TS_ReturnType
tslin_start_lin_channel.errcheck = check_status_operation

tslin_stop_lin_channel = dll.tslin_stop_lin_channel
tslin_stop_lin_channel.argtypes = [s32]
tslin_stop_lin_channel.restype = TS_ReturnType
tslin_stop_lin_channel.errcheck = check_status_operation

# Eth
# ETH Function
tsapp_set_ethernet_channel_count = dll.tsapp_set_ethernet_channel_count
tsapp_set_ethernet_channel_count.argtypes = [s32]
tsapp_set_ethernet_channel_count.restype = TS_ReturnType
tsapp_set_ethernet_channel_count.errcheck = check_status_operation

tsapp_get_ethernet_channel_count= dll.tsapp_get_ethernet_channel_count
tsapp_get_ethernet_channel_count.argtypes = [ps32]
tsapp_get_ethernet_channel_count.restype = TS_ReturnType
tsapp_get_ethernet_channel_count.errcheck = check_status_operation

tsapp_ethernet_channel_compress_mode= dll.tsapp_ethernet_channel_compress_mode
tsapp_ethernet_channel_compress_mode.argtypes = [s32,c_bool]
tsapp_ethernet_channel_compress_mode.restype = TS_ReturnType
tsapp_ethernet_channel_compress_mode.errcheck = check_status_operation

tsapp_transmit_ethernet_async = dll.tsapp_transmit_ethernet_async
tsapp_transmit_ethernet_async.argtypes = [PLIBEthernetHeader]
tsapp_transmit_ethernet_async.restype = TS_ReturnType
tsapp_transmit_ethernet_async.errcheck = check_status_operation

tsapp_transmit_ethernet_sync = dll.tsapp_transmit_ethernet_sync
tsapp_transmit_ethernet_sync.argtypes = [PLIBEthernetHeader,s32]
tsapp_transmit_ethernet_sync.restype = TS_ReturnType
tsapp_transmit_ethernet_sync.errcheck = check_status_operation

inject_ethernet_frame = dll.inject_ethernet_frame
inject_ethernet_frame.argtypes = [PLIBEthernetHeader]
inject_ethernet_frame.restype = TS_ReturnType
inject_ethernet_frame.errcheck = check_status_operation

tslog_blf_write_ethernet = dll.tslog_blf_write_ethernet
tslog_blf_write_ethernet.argtypes = [s32,PLIBEthernetHeader]
tslog_blf_write_ethernet.restype = TS_ReturnType
tslog_blf_write_ethernet.errcheck = check_status_operation

transmit_ethernet_async_wo_pretx = dll.transmit_ethernet_async_wo_pretx
transmit_ethernet_async_wo_pretx.argtypes = [PLIBEthernetHeader]
transmit_ethernet_async_wo_pretx.restype = TS_ReturnType
transmit_ethernet_async_wo_pretx.errcheck = check_status_operation

eth_build_ipv4_udp_packet = dll.eth_build_ipv4_udp_packet
eth_build_ipv4_udp_packet.argtypes = [PLIBEthernetHeader,pu8,pu8,u16,u16,pu8,s32,ps32,ps32]
eth_build_ipv4_udp_packet.restype = TS_ReturnType
eth_build_ipv4_udp_packet.errcheck = check_status_operation

eth_is_udp_packet = dll.eth_is_udp_packet
eth_is_udp_packet.argtypes = [PLIBEthernetHeader,u16,u16,u16,c_bool]
eth_is_udp_packet.restype = TS_ReturnType
eth_is_udp_packet.errcheck = check_status_operation

eth_ip_calc_header_checksum = dll.eth_ip_calc_header_checksum
eth_ip_calc_header_checksum.argtypes = [PLIBEthernetHeader,c_bool,u16]
eth_ip_calc_header_checksum.restype = TS_ReturnType
eth_ip_calc_header_checksum.errcheck = check_status_operation

eth_udp_calc_checksum = dll.eth_udp_calc_checksum
eth_udp_calc_checksum.argtypes = [PLIBEthernetHeader,pu8,u16,c_bool,pu16]
eth_udp_calc_checksum.restype = TS_ReturnType
eth_udp_calc_checksum.errcheck = check_status_operation

eth_udp_calc_checksum_on_frame = dll.eth_udp_calc_checksum_on_frame
eth_udp_calc_checksum_on_frame.argtypes = [PLIBEthernetHeader,c_bool,pu16]
eth_udp_calc_checksum_on_frame.restype = TS_ReturnType
eth_udp_calc_checksum_on_frame.errcheck = check_status_operation

eth_log_ethernet_frame_data = dll.eth_log_ethernet_frame_data
eth_log_ethernet_frame_data.argtypes = [PLIBEthernetHeader,c_bool]
eth_log_ethernet_frame_data.restype = TS_ReturnType
eth_log_ethernet_frame_data.errcheck = check_status_operation


set_flexray_ub_bit_auto_handle = dll.set_flexray_ub_bit_auto_handle
set_flexray_ub_bit_auto_handle.argtypes = [c_bool]
set_flexray_ub_bit_auto_handle.restype = TS_ReturnType
set_flexray_ub_bit_auto_handle.errcheck = check_status_operation

tsapp_enable_bus_statistics = dll.tsapp_enable_bus_statistics
#arg[0] AEnable : None
tsapp_enable_bus_statistics.argtypes =[c_bool]
tsapp_enable_bus_statistics.restype = s32

tsapp_clear_bus_statistics = dll.tsapp_clear_bus_statistics
tsapp_clear_bus_statistics.argtypes =[]
tsapp_clear_bus_statistics.restype = s32

tsapp_get_bus_statistics = dll.tsapp_get_bus_statistics
#arg[0] ABusType : None
#arg[1] AIdxChn : None
#arg[2] AIdxStat : None
#arg[3] AStat : None
tsapp_get_bus_statistics.argtypes =[s32,s32,s32,pdouble]
tsapp_get_bus_statistics.restype = s32

tsapp_get_fps_can = dll.tsapp_get_fps_can
#arg[0] AIdxChn : None
#arg[1] AIdentifier : None
#arg[2] AFPS : None
tsapp_get_fps_can.argtypes =[s32,s32,ps32]
tsapp_get_fps_can.restype = s32

tsapp_get_fps_canfd = dll.tsapp_get_fps_canfd
#arg[0] AIdxChn : None
#arg[1] AIdentifier : None
#arg[2] AFPS : None
tsapp_get_fps_canfd.argtypes =[s32,s32,ps32]
tsapp_get_fps_canfd.restype = s32

tsapp_get_fps_lin = dll.tsapp_get_fps_lin
#arg[0] AIdxChn : None
#arg[1] AIdentifier : None
#arg[2] AFPS : None
tsapp_get_fps_lin.argtypes =[s32,s32,ps32]
tsapp_get_fps_lin.restype = s32

if __name__ == '__main__': # for the module test purpose only
    ret = initialize_lib_tsmaster_with_project(b"TSMaster",b'D:\\software\\TOSUN\\TSMaster\\bin\\Configuration\\TOSUN\\TSMaster_CAN')
    a = c_char_p()
    tsapp_get_current_application(a)
    print(a.value) 
    tsapp_set_current_application(a)
    tsapp_get_current_application(a)
    print(a.value) 
    ret = tsapp_set_can_channel_count(33)
    b = s32()
    tsapp_get_can_channel_count(b)
    print(b)

    tsapp_set_lin_channel_count(1)
    tsapp_get_lin_channel_count(b)
    print(b)
    c = TLIBTSMapping()
    c.FAppChannelIndex = 0
    c.FAppChannelType = TLIBApplicationChannelType.APP_FlexRay
    tsapp_get_mapping(c)

    finalize_lib_tsmaster()
    