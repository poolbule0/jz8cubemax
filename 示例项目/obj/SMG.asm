;--------------------------------------------------------
; File Created by SLCC : free open source ANSI-C Compiler
; Version 3.6.0 #Sep 28 2025 (MSVC)
;--------------------------------------------------------
; SL port for the RISC core
;--------------------------------------------------------
;	.file	"C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C"
	list	p=JZ8P2615
	radix dec
	include "JZ8P2615.inc"
;--------------------------------------------------------
; external declarations
;--------------------------------------------------------
	extern	_ADC_GetValue
	extern	_sw_adcBatVal
	extern	_RSRbits
	extern	_PCHbits
	extern	_PCLbits
	extern	_STATUSbits
	extern	_TC0CONbits
	extern	_TC0Cbits
	extern	_TBRDHbits
	extern	_TBRDLbits
	extern	_CPUCONbits
	extern	_IHRCCALbits
	extern	_PORT5bits
	extern	_PORT6bits
	extern	_P5CONbits
	extern	_P6CONbits
	extern	_P5PHbits
	extern	_P6PHbits
	extern	_P5PDbits
	extern	_P6PDbits
	extern	_P6ODbits
	extern	_P6WDbits
	extern	_P5IWEbits
	extern	_P6IWEbits
	extern	_P5ADEbits
	extern	_P6ADEbits
	extern	_ADATHbits
	extern	_ADATLbits
	extern	_ADISbits
	extern	_ADCON0bits
	extern	_ADCON1bits
	extern	_WDTCONbits
	extern	_TC1CONbits
	extern	_TC1PRDLbits
	extern	_PWM1DTLbits
	extern	_TC1PRDTHbits
	extern	_TC1CHbits
	extern	_TC1CLbits
	extern	_TC2CONbits
	extern	_TC2PRDLbits
	extern	_PWM2DTLbits
	extern	_TC2PRDTHbits
	extern	_TC2CHbits
	extern	_TC2CLbits
	extern	_PWM3DTHbits
	extern	_PWM3DTLbits
	extern	_PWM4DTHbits
	extern	_PWM4DTLbits
	extern	_PWMISbits
	extern	_DEADCONbits
	extern	_PWMCONbits
	extern	_DEADT0bits
	extern	_DEADT1bits
	extern	_INTE0bits
	extern	_INTE1bits
	extern	_INTF0bits
	extern	_INTF1bits
	extern	_IARbits
	extern	_U_Flage1
	extern	_r_g_workMod
	extern	_r_g_batVal
	extern	_r_buff
	extern	_RSR
	extern	_PCH
	extern	_PCL
	extern	_STATUS
	extern	_TC0CON
	extern	_TC0C
	extern	_TBRDH
	extern	_TBRDL
	extern	_CPUCON
	extern	_IHRCCAL
	extern	_PORT5
	extern	_PORT6
	extern	_P5CON
	extern	_P6CON
	extern	_P5PH
	extern	_P6PH
	extern	_P5PD
	extern	_P6PD
	extern	_P6OD
	extern	_P6WD
	extern	_P5IWE
	extern	_P6IWE
	extern	_P5ADE
	extern	_P6ADE
	extern	_ADATH
	extern	_ADATL
	extern	_ADIS
	extern	_ADCON0
	extern	_ADCON1
	extern	_WDTCON
	extern	_TC1CON
	extern	_TC1PRDL
	extern	_PWM1DTL
	extern	_TC1PRDTH
	extern	_TC1CH
	extern	_TC1CL
	extern	_TC2CON
	extern	_TC2PRDL
	extern	_PWM2DTL
	extern	_TC2PRDTH
	extern	_TC2CH
	extern	_TC2CL
	extern	_PWM3DTH
	extern	_PWM3DTL
	extern	_PWM4DTH
	extern	_PWM4DTL
	extern	_PWMIS
	extern	_DEADCON
	extern	_PWMCON
	extern	_DEADT0
	extern	_DEADT1
	extern	_INTE0
	extern	_INTE1
	extern	_INTF0
	extern	_INTF1
	extern	_IAR

	extern STK06
	extern STK05
	extern STK04
	extern STK03
	extern STK02
	extern STK01
	extern STK00
;--------------------------------------------------------
; global declarations
;--------------------------------------------------------
	global	_SMG_Scan
	global	_SMG_Display
	global	_Flag_Led1
	global	_Flag_Led2
	global	_Flag_Led3
	global	_Flag_Led4
	global	_smg_cnt
	global	_t_ledCntTab

;--------------------------------------------------------
; global definitions
;--------------------------------------------------------
UD_SMG_0	udata
_Flag_Led1	res	1

UD_SMG_1	udata
_Flag_Led2	res	1

UD_SMG_2	udata
_Flag_Led3	res	1

UD_SMG_3	udata
_Flag_Led4	res	1

;--------------------------------------------------------
; absolute symbol definitions
;--------------------------------------------------------
;--------------------------------------------------------
; compiler-defined variables
;--------------------------------------------------------
UDL_SMG_0	udata
r0x1005	res	1
r0x1006	res	1
r0x1007	res	1
r0x1008	res	1
r0x1009	res	1
r0x100A	res	1
;--------------------------------------------------------
; initialized data
;--------------------------------------------------------

ID_SMG_0	idata
_smg_cnt
	add 0x182,a
	db	0x00


ID_SMG_1	code
_t_ledCntTab
	add 0x182,a
	retl 0x3f
	retl 0x06
	retl 0x5b
	retl 0x4f
	retl 0x66
	retl 0x6d
	retl 0x7d
	retl 0x07
	retl 0x7f
	retl 0x6f
	retl 0x00


;@Allocation info for local variables in function 'SMG_Display'
;@SMG_Display SMG_Scan                  Allocated to registers ;size:2
;@SMG_Display ADC_GetValue              Allocated to registers ;size:2
;@SMG_Display sw_adcBatVal              Allocated to registers ;size:2
;@SMG_Display RSRbits                   Allocated to registers ;size:1
;@SMG_Display PCHbits                   Allocated to registers ;size:1
;@SMG_Display PCLbits                   Allocated to registers ;size:1
;@SMG_Display STATUSbits                Allocated to registers ;size:1
;@SMG_Display TC0CONbits                Allocated to registers ;size:1
;@SMG_Display TC0Cbits                  Allocated to registers ;size:1
;@SMG_Display TBRDHbits                 Allocated to registers ;size:1
;@SMG_Display TBRDLbits                 Allocated to registers ;size:1
;@SMG_Display CPUCONbits                Allocated to registers ;size:1
;@SMG_Display IHRCCALbits               Allocated to registers ;size:1
;@SMG_Display PORT5bits                 Allocated to registers ;size:1
;@SMG_Display PORT6bits                 Allocated to registers ;size:1
;@SMG_Display P5CONbits                 Allocated to registers ;size:1
;@SMG_Display P6CONbits                 Allocated to registers ;size:1
;@SMG_Display P5PHbits                  Allocated to registers ;size:1
;@SMG_Display P6PHbits                  Allocated to registers ;size:1
;@SMG_Display P5PDbits                  Allocated to registers ;size:1
;@SMG_Display P6PDbits                  Allocated to registers ;size:1
;@SMG_Display P6ODbits                  Allocated to registers ;size:1
;@SMG_Display P6WDbits                  Allocated to registers ;size:1
;@SMG_Display P5IWEbits                 Allocated to registers ;size:1
;@SMG_Display P6IWEbits                 Allocated to registers ;size:1
;@SMG_Display P5ADEbits                 Allocated to registers ;size:1
;@SMG_Display P6ADEbits                 Allocated to registers ;size:1
;@SMG_Display ADATHbits                 Allocated to registers ;size:1
;@SMG_Display ADATLbits                 Allocated to registers ;size:1
;@SMG_Display ADISbits                  Allocated to registers ;size:1
;@SMG_Display ADCON0bits                Allocated to registers ;size:1
;@SMG_Display ADCON1bits                Allocated to registers ;size:1
;@SMG_Display WDTCONbits                Allocated to registers ;size:1
;@SMG_Display TC1CONbits                Allocated to registers ;size:1
;@SMG_Display TC1PRDLbits               Allocated to registers ;size:1
;@SMG_Display PWM1DTLbits               Allocated to registers ;size:1
;@SMG_Display TC1PRDTHbits              Allocated to registers ;size:1
;@SMG_Display TC1CHbits                 Allocated to registers ;size:1
;@SMG_Display TC1CLbits                 Allocated to registers ;size:1
;@SMG_Display TC2CONbits                Allocated to registers ;size:1
;@SMG_Display TC2PRDLbits               Allocated to registers ;size:1
;@SMG_Display PWM2DTLbits               Allocated to registers ;size:1
;@SMG_Display TC2PRDTHbits              Allocated to registers ;size:1
;@SMG_Display TC2CHbits                 Allocated to registers ;size:1
;@SMG_Display TC2CLbits                 Allocated to registers ;size:1
;@SMG_Display PWM3DTHbits               Allocated to registers ;size:1
;@SMG_Display PWM3DTLbits               Allocated to registers ;size:1
;@SMG_Display PWM4DTHbits               Allocated to registers ;size:1
;@SMG_Display PWM4DTLbits               Allocated to registers ;size:1
;@SMG_Display PWMISbits                 Allocated to registers ;size:1
;@SMG_Display DEADCONbits               Allocated to registers ;size:1
;@SMG_Display PWMCONbits                Allocated to registers ;size:1
;@SMG_Display DEADT0bits                Allocated to registers ;size:1
;@SMG_Display DEADT1bits                Allocated to registers ;size:1
;@SMG_Display INTE0bits                 Allocated to registers ;size:1
;@SMG_Display INTE1bits                 Allocated to registers ;size:1
;@SMG_Display INTF0bits                 Allocated to registers ;size:1
;@SMG_Display INTF1bits                 Allocated to registers ;size:1
;@SMG_Display IARbits                   Allocated to registers ;size:1
;@SMG_Display U_Flage1                  Allocated to registers ;size:1
;@SMG_Display r_g_workMod               Allocated to registers ;size:1
;@SMG_Display r_g_batVal                Allocated to registers ;size:1
;@SMG_Display r_buff                    Allocated to registers ;size:1
;@SMG_Display Flag_Led1                 Allocated to registers ;size:1
;@SMG_Display Flag_Led2                 Allocated to registers ;size:1
;@SMG_Display Flag_Led3                 Allocated to registers ;size:1
;@SMG_Display Flag_Led4                 Allocated to registers ;size:1
;@SMG_Display smg_cnt                   Allocated to registers ;size:1
;@SMG_Display b                         Allocated to registers ;size:1
;@SMG_Display a                         Allocated to registers r0x1005 ;size:1
;@SMG_Display smg_bai                   Allocated to registers r0x1007 ;size:1
;@SMG_Display smg_shi                   Allocated to registers r0x1008 ;size:1
;@SMG_Display smg_ge                    Allocated to registers r0x1009 ;size:1
;@SMG_Display smg_tu                    Allocated to registers r0x1006 ;size:1
;@SMG_Display smg_buff                  Allocated to registers r0x1005 ;size:1
;@SMG_Display RSR                       Allocated to registers ;size:1
;@SMG_Display PCH                       Allocated to registers ;size:1
;@SMG_Display PCL                       Allocated to registers ;size:1
;@SMG_Display STATUS                    Allocated to registers ;size:1
;@SMG_Display TC0CON                    Allocated to registers ;size:1
;@SMG_Display TC0C                      Allocated to registers ;size:1
;@SMG_Display TBRDH                     Allocated to registers ;size:1
;@SMG_Display TBRDL                     Allocated to registers ;size:1
;@SMG_Display CPUCON                    Allocated to registers ;size:1
;@SMG_Display IHRCCAL                   Allocated to registers ;size:1
;@SMG_Display PORT5                     Allocated to registers ;size:1
;@SMG_Display PORT6                     Allocated to registers ;size:1
;@SMG_Display P5CON                     Allocated to registers ;size:1
;@SMG_Display P6CON                     Allocated to registers ;size:1
;@SMG_Display P5PH                      Allocated to registers ;size:1
;@SMG_Display P6PH                      Allocated to registers ;size:1
;@SMG_Display P5PD                      Allocated to registers ;size:1
;@SMG_Display P6PD                      Allocated to registers ;size:1
;@SMG_Display P6OD                      Allocated to registers ;size:1
;@SMG_Display P6WD                      Allocated to registers ;size:1
;@SMG_Display P5IWE                     Allocated to registers ;size:1
;@SMG_Display P6IWE                     Allocated to registers ;size:1
;@SMG_Display P5ADE                     Allocated to registers ;size:1
;@SMG_Display P6ADE                     Allocated to registers ;size:1
;@SMG_Display ADATH                     Allocated to registers ;size:1
;@SMG_Display ADATL                     Allocated to registers ;size:1
;@SMG_Display ADIS                      Allocated to registers ;size:1
;@SMG_Display ADCON0                    Allocated to registers ;size:1
;@SMG_Display ADCON1                    Allocated to registers ;size:1
;@SMG_Display WDTCON                    Allocated to registers ;size:1
;@SMG_Display TC1CON                    Allocated to registers ;size:1
;@SMG_Display TC1PRDL                   Allocated to registers ;size:1
;@SMG_Display PWM1DTL                   Allocated to registers ;size:1
;@SMG_Display TC1PRDTH                  Allocated to registers ;size:1
;@SMG_Display TC1CH                     Allocated to registers ;size:1
;@SMG_Display TC1CL                     Allocated to registers ;size:1
;@SMG_Display TC2CON                    Allocated to registers ;size:1
;@SMG_Display TC2PRDL                   Allocated to registers ;size:1
;@SMG_Display PWM2DTL                   Allocated to registers ;size:1
;@SMG_Display TC2PRDTH                  Allocated to registers ;size:1
;@SMG_Display TC2CH                     Allocated to registers ;size:1
;@SMG_Display TC2CL                     Allocated to registers ;size:1
;@SMG_Display PWM3DTH                   Allocated to registers ;size:1
;@SMG_Display PWM3DTL                   Allocated to registers ;size:1
;@SMG_Display PWM4DTH                   Allocated to registers ;size:1
;@SMG_Display PWM4DTL                   Allocated to registers ;size:1
;@SMG_Display PWMIS                     Allocated to registers ;size:1
;@SMG_Display DEADCON                   Allocated to registers ;size:1
;@SMG_Display PWMCON                    Allocated to registers ;size:1
;@SMG_Display DEADT0                    Allocated to registers ;size:1
;@SMG_Display DEADT1                    Allocated to registers ;size:1
;@SMG_Display INTE0                     Allocated to registers ;size:1
;@SMG_Display INTE1                     Allocated to registers ;size:1
;@SMG_Display INTF0                     Allocated to registers ;size:1
;@SMG_Display INTF1                     Allocated to registers ;size:1
;@SMG_Display IAR                       Allocated to registers ;size:1
;@end Allocation info for local variables in function 'SMG_Display';

;--------------------------------------------------------
; overlayable items in internal ram 
;--------------------------------------------------------
;	udata_ovr
;--------------------------------------------------------
; code
;--------------------------------------------------------
code_SMG	code
;***
;  pBlock Stats: dbName = C
;***
;has an exit
;; Starting pCode block
S_SMG__SMG_Scan	code
_SMG_Scan:	;Function start
; 2 exit points
;	.line	60; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	IO_IN();
	BTS	_P5CONbits,2
	BTS	_P5CONbits,1
	BTS	_P5CONbits,0
	BTS	_P6CONbits,7
	BTS	_P6CONbits,6
;;swapping arguments (AOP_TYPEs 1/3)
;	.line	61; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	switch(smg_cnt)
	MOV	A,@0x12
	SUB	A,_smg_cnt
	JBTC	STATUS,0
	JMP	_00176_DS_
	MOV	A,_smg_cnt
	BANKSEL	PCL
	ADD	PCL,A
	JMP	_00121_DS_
	JMP	_00124_DS_
	JMP	_00127_DS_
	JMP	_00130_DS_
	JMP	_00133_DS_
	JMP	_00136_DS_
	JMP	_00139_DS_
	JMP	_00142_DS_
	JMP	_00145_DS_
	JMP	_00148_DS_
	JMP	_00151_DS_
	JMP	_00154_DS_
	JMP	_00157_DS_
	JMP	_00160_DS_
	JMP	_00163_DS_
	JMP	_00166_DS_
	JMP	_00169_DS_
	JMP	_00172_DS_
_00121_DS_:
;	.line	64; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	if(B1_LED)
	JBTS	_Flag_Led1,1
	JMP	_00123_DS_
;	.line	66; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN3_H();
	BTS	_PORT5bits,0
	BTC	_P5CONbits,0
	BTS	_PORT5bits,0
_00123_DS_:
;	.line	68; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN4_L();
	BTC	_PORT6bits,7
	BTC	_P6CONbits,7
	BTC	_PORT6bits,7
;	.line	69; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	break;
	JMP	_00176_DS_
_00124_DS_:
;	.line	71; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	if (C1_LED)
	JBTS	_Flag_Led1,2
	JMP	_00126_DS_
;	.line	73; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN4_L();
	BTC	_PORT6bits,7
	BTC	_P6CONbits,7
	BTC	_PORT6bits,7
_00126_DS_:
;	.line	75; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN2_H();
	BTS	_PORT5bits,1
	BTC	_P5CONbits,1
	BTS	_PORT5bits,1
;	.line	76; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	break;
	JMP	_00176_DS_
_00127_DS_:
;	.line	78; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	if (A2_LED)
	JBTS	_Flag_Led2,0
	JMP	_00129_DS_
;	.line	80; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN3_L();
	BTC	_PORT5bits,0
	BTC	_P5CONbits,0
	BTC	_PORT5bits,0
_00129_DS_:
;	.line	82; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN2_H();
	BTS	_PORT5bits,1
	BTC	_P5CONbits,1
	BTS	_PORT5bits,1
;	.line	83; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	break;
	JMP	_00176_DS_
_00130_DS_:
;	.line	85; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	if (B2_LED)
	JBTS	_Flag_Led2,1
	JMP	_00132_DS_
;	.line	87; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN2_L();
	BTC	_PORT5bits,1
	BTC	_P5CONbits,1
	BTC	_PORT5bits,1
_00132_DS_:
;	.line	89; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN3_H();
	BTS	_PORT5bits,0
	BTC	_P5CONbits,0
	BTS	_PORT5bits,0
;	.line	90; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	break;
	JMP	_00176_DS_
_00133_DS_:
;	.line	92; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	if (C2_LED)
	JBTS	_Flag_Led2,2
	JMP	_00135_DS_
;	.line	94; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN3_L();
	BTC	_PORT5bits,0
	BTC	_P5CONbits,0
	BTC	_PORT5bits,0
_00135_DS_:
;	.line	96; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN4_H();
	BTS	_PORT6bits,7
	BTC	_P6CONbits,7
	BTS	_PORT6bits,7
;	.line	97; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	break;
	JMP	_00176_DS_
_00136_DS_:
;	.line	99; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	if (D2_LED)
	JBTS	_Flag_Led2,3
	JMP	_00138_DS_
;	.line	101; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN2_L();
	BTC	_PORT5bits,1
	BTC	_P5CONbits,1
	BTC	_PORT5bits,1
_00138_DS_:
;	.line	103; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN4_H();
	BTS	_PORT6bits,7
	BTC	_P6CONbits,7
	BTS	_PORT6bits,7
;	.line	104; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	break;
	JMP	_00176_DS_
_00139_DS_:
;	.line	106; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	if (E2_LED)
	JBTS	_Flag_Led2,4
	JMP	_00141_DS_
;	.line	108; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN2_L();
	BTC	_PORT5bits,1
	BTC	_P5CONbits,1
	BTC	_PORT5bits,1
_00141_DS_:
;	.line	110; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN5_H();
	BTS	_PORT6bits,6
	BTC	_P6CONbits,6
	BTS	_PORT6bits,6
;	.line	111; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	break;
	JMP	_00176_DS_
_00142_DS_:
;	.line	113; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	if (F2_LED)
	JBTS	_Flag_Led2,5
	JMP	_00144_DS_
;	.line	115; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN3_L();
	BTC	_PORT5bits,0
	BTC	_P5CONbits,0
	BTC	_PORT5bits,0
_00144_DS_:
;	.line	117; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN5_H();
	BTS	_PORT6bits,6
	BTC	_P6CONbits,6
	BTS	_PORT6bits,6
;	.line	118; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	break;
	JMP	_00176_DS_
_00145_DS_:
;	.line	120; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	if (G2_LED)
	JBTS	_Flag_Led2,6
	JMP	_00147_DS_
;	.line	122; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN4_L();
	BTC	_PORT6bits,7
	BTC	_P6CONbits,7
	BTC	_PORT6bits,7
_00147_DS_:
;	.line	124; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN5_H();
	BTS	_PORT6bits,6
	BTC	_P6CONbits,6
	BTS	_PORT6bits,6
;	.line	125; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	break;
	JMP	_00176_DS_
_00148_DS_:
;	.line	127; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	if (A3_LED)
	JBTS	_Flag_Led3,0
	JMP	_00150_DS_
;	.line	129; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN2_L();
	BTC	_PORT5bits,1
	BTC	_P5CONbits,1
	BTC	_PORT5bits,1
_00150_DS_:
;	.line	131; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN1_H();
	BTS	_PORT5bits,2
	BTC	_P5CONbits,2
	BTS	_PORT5bits,2
;	.line	132; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	break;
	JMP	_00176_DS_
_00151_DS_:
;	.line	134; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	if (B3_LED)
	JBTS	_Flag_Led3,1
	JMP	_00153_DS_
;	.line	136; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN1_L();
	BTC	_PORT5bits,2
	BTC	_P5CONbits,2
	BTC	_PORT5bits,2
_00153_DS_:
;	.line	138; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN2_H();
	BTS	_PORT5bits,1
	BTC	_P5CONbits,1
	BTS	_PORT5bits,1
;	.line	139; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	break;
	JMP	_00176_DS_
_00154_DS_:
;	.line	141; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	if (C3_LED)
	JBTS	_Flag_Led3,2
	JMP	_00156_DS_
;	.line	143; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN3_L();
	BTC	_PORT5bits,0
	BTC	_P5CONbits,0
	BTC	_PORT5bits,0
_00156_DS_:
;	.line	145; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN1_H();
	BTS	_PORT5bits,2
	BTC	_P5CONbits,2
	BTS	_PORT5bits,2
;	.line	146; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	break;
	JMP	_00176_DS_
_00157_DS_:
;	.line	148; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	if (D3_LED)
	JBTS	_Flag_Led3,3
	JMP	_00159_DS_
;	.line	150; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN1_L();
	BTC	_PORT5bits,2
	BTC	_P5CONbits,2
	BTC	_PORT5bits,2
_00159_DS_:
;	.line	152; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN3_H();
	BTS	_PORT5bits,0
	BTC	_P5CONbits,0
	BTS	_PORT5bits,0
;	.line	153; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	break;
	JMP	_00176_DS_
_00160_DS_:
;	.line	155; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	if (E3_LED)
	JBTS	_Flag_Led3,4
	JMP	_00162_DS_
;	.line	157; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN4_L();
	BTC	_PORT6bits,7
	BTC	_P6CONbits,7
	BTC	_PORT6bits,7
_00162_DS_:
;	.line	159; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN1_H();
	BTS	_PORT5bits,2
	BTC	_P5CONbits,2
	BTS	_PORT5bits,2
;	.line	160; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	break;
	JMP	_00176_DS_
_00163_DS_:
;	.line	162; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	if (F3_LED)
	JBTS	_Flag_Led3,5
	JMP	_00165_DS_
;	.line	164; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN1_L();
	BTC	_PORT5bits,2
	BTC	_P5CONbits,2
	BTC	_PORT5bits,2
_00165_DS_:
;	.line	166; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN4_H();
	BTS	_PORT6bits,7
	BTC	_P6CONbits,7
	BTS	_PORT6bits,7
;	.line	167; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	break;
	JMP	_00176_DS_
_00166_DS_:
;	.line	169; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	if (G3_LED)
	JBTS	_Flag_Led3,6
	JMP	_00168_DS_
;	.line	171; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN1_L();
	BTC	_PORT5bits,2
	BTC	_P5CONbits,2
	BTC	_PORT5bits,2
_00168_DS_:
;	.line	173; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN5_H();
	BTS	_PORT6bits,6
	BTC	_P6CONbits,6
	BTS	_PORT6bits,6
;	.line	174; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	break;
	JMP	_00176_DS_
_00169_DS_:
;	.line	176; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	if (B_LED_LIGHTING)
	JBTS	_Flag_Led4,0
	JMP	_00171_DS_
;	.line	178; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN5_L();
	BTC	_PORT6bits,6
	BTC	_P6CONbits,6
	BTC	_PORT6bits,6
_00171_DS_:
;	.line	180; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN3_H();
	BTS	_PORT5bits,0
	BTC	_P5CONbits,0
	BTS	_PORT5bits,0
;	.line	181; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	break;
	JMP	_00176_DS_
_00172_DS_:
;	.line	183; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	if (B_LED_PERCENT_SIGNS)
	JBTS	_Flag_Led4,1
	JMP	_00174_DS_
;	.line	185; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN5_L();
	BTC	_PORT6bits,6
	BTC	_P6CONbits,6
	BTC	_PORT6bits,6
_00174_DS_:
;	.line	187; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	PIN2_H();
	BTS	_PORT5bits,1
	BTC	_P5CONbits,1
	BTS	_PORT5bits,1
_00176_DS_:
;	.line	195; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	if (++ smg_cnt > 17)
	INC	_smg_cnt
;;swapping arguments (AOP_TYPEs 1/3)
	MOV	A,@0x12
	SUB	A,_smg_cnt
	JBTS	STATUS,0
	JMP	_00179_DS_
;	.line	197; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	smg_cnt = 0;
	CLR	_smg_cnt
;	.line	200; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	}
_00179_DS_:
	RET	
; exit point of _SMG_Scan

;***
;  pBlock Stats: dbName = C
;***
;has an exit
;functions called:
;   (_t_ledCntTab + 0)
;   (_t_ledCntTab + 0)
;   (_t_ledCntTab + 0)
;   (_t_ledCntTab + 0)
;   (_t_ledCntTab + 0)
;   (_t_ledCntTab + 0)
;7 compiler assigned registers:
;   r0x1005
;   STK00
;   r0x1006
;   r0x1007
;   r0x1008
;   r0x1009
;   r0x100A
;; Starting pCode block
S_SMG__SMG_Display	code
_SMG_Display:	;Function start
; 2 exit points
;	.line	19; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	void SMG_Display(uint8_t a ,uint8_t b)
	MOV	r0x1005,A
	MOV	A,STK00
	MOV	r0x1006,A
;	.line	21; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	uint8_t smg_bai = 10;
	MOV	A,@0x0a
	MOV	r0x1007,A
;	.line	29; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	if(smg_buff >= 100)
	MOV	A,@0x64
	SUB	A,r0x1005
	JBTS	STATUS,0
	JMP	_00115_DS_
;	.line	31; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	smg_bai = 1;
	MOV	A,@0x01
	MOV	r0x1007,A
;	.line	32; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	smg_shi = 0;
	CLR	r0x1008
;	.line	33; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	smg_ge = 0;
	CLR	r0x1009
	JMP	_00110_DS_
_00115_DS_:
;	.line	37; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	while(smg_buff >= 10)
	CLR	r0x100A
_00105_DS_:
	MOV	A,@0x0a
	SUB	A,r0x1005
	JBTS	STATUS,0
	JMP	_00116_DS_
;	.line	39; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	smg_buff -= 10;
	MOV	A,@0xf6
	ADD	r0x1005,A
;	.line	40; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	smg_shi++;
	INC	r0x100A
	JMP	_00105_DS_
_00116_DS_:
	MOV	A,r0x100A
	MOV	r0x1008,A
;	.line	42; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	smg_ge = smg_buff;
	MOV	A,r0x1005
	MOV	r0x1009,A
_00110_DS_:
;	.line	45; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	smg_bai = t_ledCntTab[smg_bai];
	MOV	A,r0x1007
	CALL	(_t_ledCntTab + 0)
	MOV	r0x1007,A
;	.line	46; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	smg_shi = t_ledCntTab[smg_shi];
	MOV	A,r0x1008
	CALL	(_t_ledCntTab + 0)
	MOV	r0x1008,A
;	.line	47; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	smg_ge = t_ledCntTab[smg_ge];
	MOV	A,r0x1009
	CALL	(_t_ledCntTab + 0)
	MOV	r0x1009,A
;;gen.c:6919: size=0, offset=0, AOP_TYPE(res)=8
;	.line	49; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	SMG_BAI = smg_bai;
	MOV	A,r0x1007
	MOV	(_Flag_Led1 + 0),A
;;gen.c:6919: size=0, offset=0, AOP_TYPE(res)=8
;	.line	50; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	SMG_SHI = smg_shi;
	MOV	A,r0x1008
	MOV	(_Flag_Led2 + 0),A
;;gen.c:6919: size=0, offset=0, AOP_TYPE(res)=8
;	.line	51; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	SMG_GE = smg_ge;
	MOV	A,r0x1009
	MOV	(_Flag_Led3 + 0),A
;;gen.c:6919: size=0, offset=0, AOP_TYPE(res)=8
;	.line	52; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	SMG_TU = smg_tu;
	MOV	A,r0x1006
	MOV	(_Flag_Led4 + 0),A
;	.line	55; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SMG.C	}
	RET	
; exit point of _SMG_Display


;	code size estimation:
;	  242+    1 =   243 instructions (  488 byte)

	end
