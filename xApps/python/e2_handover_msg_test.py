#!/usr/bin/env python3
import argparse
import signal
from lib.xAppBase import xAppBase

metric_to_unit = {
    "RSRP": "dBm",
    "RSRQ": "dB",
    "CQI": "-",
    "RRU.PrbTotDl": "-",
    "DRB.RlcSduTransmittedVolumeDL": "kbit",
    "DRB.RlcSduTransmittedVolumeUL": "kbit",
    #"DRB.AirIfDelayDl": "ms",
    #"DRB.AirIfDelayDist": "-",
    #"DRB.AirIfDelayUl": "ms",
    #"DRB.RlcDelayUl": "ms",
    #"DRB.PdcpReordDelayUl": "ms",
    #"DRB.DelayDlNgranUeDist": "-",
    #"DRB.DelayUlNgranUeDist": "-",
    #"DRB.DelayUlNgranUeIncD1Dist": "-",
    #"GTP.DelayDlPsaUpfNgranMean": "us",
    #"GTP.DelayDlPsaUpfNgranDist": "-",
    #"RRU.PrbTotDl": "%",
    #"RRU.PrbTotUl": "%",
    #"RRU.PrbTotDlDist": "%",
    #"RRU.PrbTotUlDist": "%",
    #"RRU.PrbUsedDl": "-",
    #"RRU.PrbAvailDl": "-",
    #"RRU.PrbUsedUl": "-",
    #"RRU.PrbAvailUl": "-",
    #"RRU.MaxPrbUsedDl": "-",
    #"RRU.MaxPrbUsedUl": "-",
    #"RRU.PrbTotDlMimo": "%",
    #"RRU.PrbTotUlMimo": "%",
    #"RRU.PrbTotSdmDl": "%",
    #"RRU.PrbTotSdmUl": "%",
    "DRB.UEThpDl": "kbps",
    #"DRB.UEThpDlDist": "-",
    "DRB.UEThpUl": "kbps",
    #"DRB.UEThpUlDist": "-",
    #"DRB.UEUnresVolDl": "%",
    #"DRB.UEUnresVolUl": "%",
    #"DRB.PDCP.UEThpDl": "kbps",
    #"RRC.ConnMean": "-",
    #"RRC.ConnMax": "%",
    #"RRC.InactiveConnMean": "-",
    #"RRC.InactiveConnMax": "-",
    #"SM.PDUSessionSetupReq": "-",
    #"SM.PDUSessionSetupSucc": "-",
    #"SM.PDUSessionSetupFail": "-",
    #"SM.MeanPDUSessionSetupReq": "-",
    #"SM.MaxPDUSessionSetupReq": "-",
    #"MM.HoPrepInterReq": "-",
    #"MM.HoPrepInterSucc": "-",
    #"MM.HoPrepInterFail": "-",
    #"MM.HoResAlloInterReq": "-",
    #"MM.HoResAlloInterSucc": "-",
    #"MM.HoResAlloInterFail": "-",
    #"MM.HoExeInterReq": "-",
    #"MM.HoExeInterSucc": "-",
    #"MM.HoExeInterFail": "-",
    #"MM.HoExeInterReq.TimeMean": "ms",
    #"MM.HoExeInterReq.TimeMax": "ms",
    #"MM.HoExeInterSSBSucc": "-",
    #"MM.HoExeInterSSBFail": "-",
    #"MM.HoExeIntraReq": "-",
    #"MM.HoExeIntraSucc": "-",
    #"MM.HoOut5gsToEpsPrepReq": "-",
    #"MM.HoOut5gsToEpsPrepSucc": "-",
    #"MM.HoOut5gsToEpsPrepFail": "-",
    #"MM.HoIncEpsTo5gsResAlloReq": "-",
    #"MM.HoIncEpsTo5gsResAlloSucc": "-",
    #"MM.HoIncEpsTo5gsResAlloFail": "-",
    #"MM.HoOutExe5gsToEpsReq": "-",
    #"MM.HoOutExe5gsToEpsSucc": "-",
    #"MM.HoOutExe5gsToEpsFail": "-",
    #"MM.HoOut5gsToEpsFallbackPrepReq": "-",
    #"MM.HoOut5gsToEpsFallbackPrepSucc": "-",
    #"MM.HoOut5gsToEpsFallbackPrepFail": "-",
    #"MM.HoOutExe5gsToEpsFallbackSucc": "-",
    #"MM.HoOutExe5gsToEpsFallbackFail": "-",
    #"MM.Ho5gsToEpsFallbackTimeMean": "ms",
    #"MM.HoExeHo5gsToEpsFallbackTimeMean": "ms",
    #"MM.Redirection.5gsToEpsFallback": "-",
    #"MM.HoExeIntraFreqReq": "-",
    #"MM.HoExeIntraFreqSucc": "-",
    #"MM.HoExeInterFreqReq": "-",
    #"MM.HoExeInterFreqSucc": "-",
    #"MM.ChoPrepInterReq": "-",
    #"MM.ChoPrepInterSucc": "-",
    #"MM.ChoPrepInterFail": "-",
    #"MM.ChoResAlloInterReq": "-",
    #"MM.ChoResAlloInterSucc": "-",
    #"MM.ChoResAlloInterFail": "-",
    #"MM.ConfigInterReqCho": "-",
    #"MM.ConfigInterReqChoUes": "-",
    #"MM.ChoExeInterSucc": "-",
    #"MM.ChoExeInterReq.TimeMean": "ms",
    #"MM.ChoExeInterReq.TimeMax": "ms",
    #"MM.ChoPrepInterReqUes": "-",
    #"MM.ChoPrepInterSuccUes": "-",
    #"MM.ChoPrepInterFailUes": "-",
    #"MM.ConfigIntraReqCho": "-",
    #"MM.ConfigIntraReqChoUes": "-",
    #"MM.ChoExeIntraSucc": "-",
    #"MM.DapsHoPrepInterReq": "-",
    #"MM.DapsHoPrepInterSucc": "-",
    #"MM.DapsHoPrepInterFail": "-",
    #"MM.DapsHoResAlloInterReq": "-",
    #"MM.DapsHoResAlloInterSucc": "-",
    #"MM.DapsHoResAlloInterFail": "-",
    #"MM.DapsHoExeInterReq": "-",
    #"MM.DapsHoExeInterSucc": "-",
    #"MM.DapsHoExeInterFail": "-",
    #"MM.DapsHoExeIntraReq": "-",
    #"MM.DapsHoExeIntraSucc": "-",
    #"TB.TotNbrDlInitial": "-",
    #"TB.IntialErrNbrDl": "-",
    #"TB.TotNbrDl": "-",
    #"TB.ErrTotNbrDl": "-",
    #"TB.ResidualErrNbrDl": "-",
    #"TB.TotNbrUlInit": "-",
    #"TB.ErrNbrUlInitial": "-",
    #"TB.TotNbrUl": "-",
    #"TB.ErrTotNbrUl": "-",
    #"TB.ResidualErrNbrUl": "-",
    #"DRB.EstabAtt": "-",
    #"DRB.EstabSucc": "-",
    #"DRB.RelActNbr": "-",
    #"DRB.SessionTime": "ms",
    #"DRB.InitialEstabAtt": "-",
    #"DRB.InitialEstabSucc": "-",
    #"DRB.ResumeAtt": "-",
    #"DRB.ResumeSucc": "-",
    #"DRB.MeanEstabSucc": "-",
    #"DRB.MaxEstabSucc": "-",
    #"DRB.GTPUPathFailure": "-",
    #"DRB.EstabAttDC": "-",
    #"DRB.EstabSuccDC": "-",
    #"CARR.WBCQIDist": "-",
    #"CARR.PDSCHMCSDist": "-",
    #"CARR.PUSCHMCSDist": "-",
    #"CARR.MUPDSCHMCSDist": "-",
    #"CARR.MUPUSCHMCSDist": "-",
    #"QF.RelActNbr": "-",
    #"QF.ReleaseAttNbr": "-",
    #"QF.SessionTimeQoS": "ms",
    #"QF.SessionTimeUE": "ms",
    #"QF.EstabAttNbr": "-",
    #"QF.EstabSuccNbr": "-",
    #"QF.EstabFailNbr": "-",
    #"QF.InitialEstabAttNbr": "-",
    #"QF.InitialEstabSuccNbr": "-",
    #"QF.InitialEstabFailNbr": "-",
    #"QF.ModNbrAtt": "-",
    #"QF.ModNbrSucc": "-",
    #"QF.ModNbrFail": "-",
    #"RRC.ConnEstabAtt": "-",
    #"RRC.ConnEstabSucc": "-",
    #"RRC.ConnEstabFailCause": "-",
    #"UECNTX.ConnEstabAtt": "-",
    #"UECNTX.ConnEstabSucc": "-",
    #"RRC.ReEstabAtt": "-",
    #"RRC.ReEstabSuccWithUeContext": "-",
    #"RRC.ReEstabSuccWithoutUeContext": "-",
    #"RRC.ReEstabFallbackToSetupAtt": "-",
    #"RRC.ResumeAtt": "-",
    #"RRC.ResumeSucc": "-",
    #"RRC.ResumeSuccByFallback": "-",
    #"RRC.ResumeFollowedbyNetworkRelease": "-",
    #"RRC.ResumeFollowedbySuspension": "-",
    #"RRC.ResumeFallbackToSetupAtt": "-",
    #"PEE.AvgPower": "W",
    #"PEE.MinPower": "W",
    #"PEE.MaxPower": "W",
    #"PEE.Energy": "kWh",
    #"PEE.AvgTemperature": "C",
    #"PEE.MinTemperature": "C",
    #"PEE.MaxTemperature": "C",
    #"PEE.Voltage": "V",
    #"PEE.Current": "A",
    #"PEE.Humidity": "%",
    #"RACH.PreambleDedCell": "-",
    #"RACH.PreambleACell": "-",
    #"RACH.PreambleBCell": "-",
    #"RACH.PreambleDed": "-",
    #"RACH.PreambleA": "-",
    #"RACH.PreambleB": "-",
    #"RACH.PreambleDist": "-",
    #"RACH.AccessDelayDist": "-",
    #"MR.IntraCellSSBSwitchReq": "-",
    #"MR.IntrCellSuccSSBSwitch": "-",
    #"L1M.SS-RSRP": "-",
    #"L1M.SS-RSRPNrNbr": "-",
    #"L1M.RSRPEutraNbr": "-",
    #"MR.NRScSRSRSRP": "-",
    #"DRB.MeanActiveUeDl": "-",
    #"DRB.MaxActiveUeDl": "-",
    #"DRB.MeanActiveUeUl": "-",
    #"DRB.MaxActiveUeUl": "-",
    #"5QI1QoSflow.Rel.Average.NormCallDuration": "ms",
    #"5QI1QoSflow.Rel.Average.AbnormCallDuration": "ms",
    #"5QI1QoSflow.Rel.NormCallDuration": "-",
    #"5QI1QoSflow.Rel.AbnormCallDuration": "-",
    #"HO.IntraSys.TooEarly": "-",
    #"HO.IntraSys.TooLate": "-",
    #"HO.IntraSys.ToWrongCell": "-",
    #"HO.InterSys.TooEarly": "-",
    #"HO.InterSys.TooLate": "-",
    #"HO.InterSys.Unnecessary": "-",
    #"HO.InterSys.PingPong": "-",
    #"HO.IntraSys.bTooEarly.NCI": "-",
    #"HO.IntraSys.bTooLate.NCI": "-",
    #"HO.IntraSys.bToWrongCell.NCI": "-",
    #"HO.InterSys.bTooLate.ECGI": "-",
    #"HO.InterSys.bUnnecessary.ECGI": "-",
    #"HO.InterSys.bPingPong.NCI": "-",
    #"L1M.PHR1": "-",
    #"PAG.ReceivedNbrCnInitiated": "-",
    #"PAG.ReceivedNbrRanIntiated": "-",
    #"PAG.ReceivedNbr": "-",
    #"PAG.DiscardedNbrCnInitiated": "-",
    #"PAG.DiscardedNbrRanInitiated": "-",
    #"PAG.DiscardedNbr": "-",
    #"L1M.SSBBeamRelatedUeNbr": "-",
    #"CARR.MaxTxPwr": "dBm",
    #"CARR.NRCellDU": "dBm",
    #"CARR.MUPDSCHRB": "-",
    #"CARR.MUPUSCHRB": "-",
    #"RRU.MaxLayerDlMimo": "-",
    #"RRU.MaxLayerUlMimo": "-",
    #"CARR.AverageLayersDl": "-",
    #"CARR.AverageLayersUl": "-",
    #"MIMOLayersDLy": "m",
    #"MIMOLayersULy": "m",
    #"PDSCHPRBsLayer": "-",
    #"PUSCHPRBsLayer": "-",
    #"MR.NRScSSRSRQ": "-",
    #"MR.SS-RSRQPerSSB": "-",
    #"MR.SS-RSRQ": "-",
    #"MR.NRScSSSINR": "-",
    #"MR.SS-SINRPerSSB": "-",
    #"MR.SS-SINR": "-",
    #"L1M.ATADist": "-",
    #"GTP.InDataPktPacketLossN3gNB": "-",
    #"DRB.PacketLossRateUu": "-",
    #"DRB.PdcpSduVolumeDL": "kbit",
    #"DRB.PdcpSduVolumeX2DL": "kbit",
    #"DRB.PdcpSduVolumeXnDL": "kbit",
    #"DRB.PdcpSduVolumeUL": "kbit",
    #"DRB.PdcpSduVolumeX2UL": "kbit",
    #"DRB.PdcpSduVolumeXnUL": "kbit",
    #"DRB.PacketSuccessRateUlgNBUu": "-",
    #"MeanTime5QI1Flow.RelDoubleNG": "ms",
    #"DRB.PacketLossRateUl": "-",
    #"DRB.F1UpacketLossRateUl": "-",
    #"DRB.F1UpacketLossRateDl": "-",
    #"DRB.PdcpPacketDropRateDl": "-",
    #"DRB.RlcPacketDropRateDl": "-",
    #"DRB.PdcpSduDelayDl": "0.1ms",
    #"DRB.PdcpF1DelayDl": "0.1ms",
    #"DRB.RlcSduDelayDl": "0.1ms",
    #"DRB.PdcpSduDelayDlDist": "-",
    #"DRB.GtpF1DelayDlDist": "-",
    #"DRB.RlcSduDelayDlDist": "-",
    #"DRB.RlcSduLatencyDl": "0.1ms",
    #"DRB.RlcSduLatencyDlDist": "-",
    #"UECNTX.RelReq": "-",
    #"UECNTX.RelCmd": "-",
    #"QosFlow.PdcpPduVolumeDL": "kbit",
    #"QosFlow.PdcpPduVolumeUL": "kbit",
    #"QosFlow.PdcpSduVolumeDl": "kbit",
    #"QosFlow.PdcpSduVolumeUl": "kbit",
    #"DRB.F1uPdcpSduVolumeDL": "kbit",
    #"DRB.X2uPdcpSduVolumeDl": "kbit",
    #"DRB.XnuPdcpSduVolumeDl": "kbit",
    #"DRB.F1uPdcpSduVolumeUL": "kbit",
    #"DRB.X2uPdcpSduVolumeUl": "kbit",
    #"DRB.XnuPdcpSduVolumeUl": "kbit",
    #"MM.HoPrepIntraReq": "-",
    #"MM.HoPrepIntraSucc": "-",
    #"MM.ChoPrepIntraReq": "-",
    #"MM.ChoPrepIntraSucc": "-",
    #"MM.DapsHoPrepIntraReq": "-",
    #"MM.DapsHoPrepIntraSucc": "-",
    #"MM.ChoPrepIntraReqUes": "-",
    #"MM.ChoPrepIntraSuccUes": "-",
    #"VR.VCpuUsageMean": "%",
    #"VR.VMemoryUsageMean": "%",
    #"VR.VDiskUsageMean": "%",
    #"DRB.RlcSduTransmittedVolumeDL": "kbit",
    #"DRB.RlcSduTransmittedVolumeUL": "kbit",
    #"DRB.PerDataVolumeDLDist": "-",
    #"DRB.PerDataVolumeULDist": "-",
    #"DRB.RlcPacketDropRateDLDist": "-",
    #"DRB.PacketLossRateULDist": "-",
    #"L1M.DL-SS-RSRP": "-",
    #"L1M.DL-SS-SINR": "-",
    #"L1M.UL-SRS-RSRP": "W",
}


class MyXapp(xAppBase):
    def __init__(self, http_server_port, rmr_port):
        super(MyXapp, self).__init__('', http_server_port, rmr_port)
        self.ue_dl_tx_data = {}
        self.min_prb_ratio = 1
        self.max_prb_ratio1 = 10
        self.max_prb_ratio2 = 100
        self.cur_ue_max_prb_ratio = {}
        self.dl_tx_data_threshold_mb = 20
        self.teste = {}

    def my_subscription_callback(self, e2_agent_id, subscription_id, indication_hdr, indication_msg, kpm_report_style, ue_id):
        indication_hdr = self.e2sm_kpm.extract_hdr_info(indication_hdr)
        meas_data = self.e2sm_kpm.extract_meas_data(indication_msg)
        #forjan... quer dizer, spoofing!
        self.teste["DRB.UEThpDl"] = self.teste.get("DRB.UEThpDl",0.1)+0.1
        self.teste["DRB.UEThpUl"] = self.teste.get("DRB.UEThpUl",-0.1)-0.1

        print("Data Monitoring:")
        print(f"Teste value: {self.teste['DRB.UEThpDl']}")
        print("  E2SM_KPM RIC Indication Content:")
        print("  -ColletStartTime: ", indication_hdr['colletStartTime'])
        print("  -Measurements Data:")
        print("  --UE_id: {}".format(ue_id))
        granulPeriod = meas_data.get("granulPeriod", None)
        if granulPeriod is not None:
            print("  ---granulPeriod: {}".format(granulPeriod))
        for (metric_name, values) in meas_data["measData"].items():
            print("  ---Metric: {}, Values: {:.1f} [{}]".format(metric_name,sum(values)+self.teste.get(metric_name, 0), metric_to_unit[metric_name]))
        print("------------------------------------------------------------------")
        print("")

    # Mark the function as xApp start function using xAppBase.start_function decorator.
    # It is required to start the internal msg receive loop.
    @xAppBase.start_function
    def start(self, e2_node_id, kpm_report_style, ue_ids, metric_names):
        report_period = 1000
        granul_period = 1000
        subscription_callback = lambda agent, sub, hdr, msg: self.my_subscription_callback(agent, sub, hdr, msg,
                                                                                           kpm_report_style, ue_ids[
                                                                                               0])  # Dummy condition that is always satisfied
        matchingUeConds = [{'testCondInfo': {'testType': ('ul-rSRP', 'true'), 'testExpr': 'lessthan',
                                             'testValue': ('valueInt', 1000)}}]
        print("Subscribe to E2 node ID: {}, RAN func: e2sm_kpm, Report Style: {}, metrics: {}".format(e2_node_id,
                                                                                                      kpm_report_style,
                                                                                                      metric_names))
        self.e2sm_kpm.subscribe_report_service_style_1(e2_node_id, report_period, metric_names, granul_period,
                                                       subscription_callback)
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='My example xApp')
    parser.add_argument("--http_server_port", type=int, default=8093, help="HTTP server listen port")
    parser.add_argument("--rmr_port", type=int, default=4560, help="RMR port")
    parser.add_argument("--e2_node_id", type=str, default='gnbd_001_001_00019b_0', help="E2 Node ID")
    parser.add_argument("--ran_func_id", type=int, default=2, help="RAN function ID")
    parser.add_argument("--kpm_report_style", type=int, default=1, help="KPM Report Style ID")
    parser.add_argument("--ue_ids", type=str, default='0', help="UE ID")
    parser.add_argument("--metrics", type=str, default=",".join(list(metric_to_unit.keys())),
                        help="Metrics name as comma-separated string")
    args = parser.parse_args()
    e2_node_id = args.e2_node_id  # TODO: get available E2 nodes from SubMgr, now the id has to be given.
    ran_func_id = args.ran_func_id  # TODO: get available E2 nodes from SubMgr, now the id has to be given.
    ue_ids = list(map(int, args.ue_ids.split(",")))  # Note: the UE id has to exist at E2 node!
    kpm_report_style = args.kpm_report_style
    metrics = args.metrics.split(",")
    myXapp = MyXapp(args.http_server_port, args.rmr_port) # Create MyXapp.
    myXapp.e2sm_kpm.set_ran_func_id(ran_func_id)  # Connect exit signals.
    signal.signal(signal.SIGQUIT, myXapp.signal_handler)
    signal.signal(signal.SIGTERM, myXapp.signal_handler)
    signal.signal(signal.SIGINT, myXapp.signal_handler)  # Start xApp.
    myXapp.start(e2_node_id, kpm_report_style, ue_ids, metrics)
    # Note: xApp will unsubscribe all active subscriptions at exit.