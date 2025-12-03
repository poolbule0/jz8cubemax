;--------------------------------------------------------
; File Created by SLCC : free open source ANSI-C Compiler
; Version 3.6.0 #Sep 28 2025 (MSVC)
;--------------------------------------------------------
; SL port for the RISC core
;--------------------------------------------------------
;	.file	"C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C"
	list	p=JZ8P2615
	radix dec
	include "JZ8P2615.inc"
;--------------------------------------------------------
; external declarations
;--------------------------------------------------------
	extern	_ADC_GetValue
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
	extern	__mulchar

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
	global	_sw_adcBatVal
	global	_r_g_batVal
	global	_r_gbatvalsum
	global	_r_gbatvalcnt
	global	_r_buff
	global	_adcValue
	global	_r_g_batValChangeCnt
	global	_r_g_batValAddCnt
	global	_r_g_batValDecCnt
	global	_r_g_batValAddShk
	global	_r_g_batValDecShk
	global	_r_g_batValChangeShkSet
	global	_t_tabBatValTab

;--------------------------------------------------------
; global definitions
;--------------------------------------------------------
UD_BAT_0	udata
_r_g_batVal	res	1

UD_BAT_1	udata
_r_gbatvalsum	res	2

UD_BAT_2	udata
_r_gbatvalcnt	res	1

UD_BAT_3	udata
_r_buff	res	1

UD_BAT_4	udata
_adcValue	res	2

UD_BAT_5	udata
_r_g_batValChangeCnt	res	1

UD_BAT_6	udata
_r_g_batValAddCnt	res	1

UD_BAT_7	udata
_r_g_batValDecCnt	res	1

UD_BAT_8	udata
_r_g_batValAddShk	res	2

UD_BAT_9	udata
_r_g_batValDecShk	res	2

UD_BAT_10	udata
_r_g_batValChangeShkSet	res	2

;--------------------------------------------------------
; absolute symbol definitions
;--------------------------------------------------------
;--------------------------------------------------------
; compiler-defined variables
;--------------------------------------------------------
UDL_BAT_0	udata
r0x1012	res	1
r0x1013	res	1
r0x1014	res	1
r0x1015	res	1
r0x1017	res	1
r0x1018	res	1
;--------------------------------------------------------
; initialized data
;--------------------------------------------------------

ID_BAT_0	code
_t_tabBatValTab
	add 0x182,a
	retl 0xdb
	retl 0x05
	retl 0xe1
	retl 0x05
	retl 0xe7
	retl 0x05
	retl 0xed
	retl 0x05
	retl 0xf3
	retl 0x05
	retl 0xfa
	retl 0x05
	retl 0x00
	retl 0x06
	retl 0x06
	retl 0x06
	retl 0x0c
	retl 0x06
	retl 0x12
	retl 0x06
	retl 0x19
	retl 0x06
	retl 0x1f
	retl 0x06
	retl 0x25
	retl 0x06
	retl 0x2b
	retl 0x06
	retl 0x31
	retl 0x06
	retl 0x38
	retl 0x06
	retl 0x3e
	retl 0x06
	retl 0x44
	retl 0x06
	retl 0x4a
	retl 0x06
	retl 0x50
	retl 0x06
	retl 0x57
	retl 0x06
	retl 0x5d
	retl 0x06
	retl 0x63
	retl 0x06
	retl 0x69
	retl 0x06
	retl 0x6f
	retl 0x06
	retl 0x76
	retl 0x06
	retl 0x7c
	retl 0x06
	retl 0x82
	retl 0x06
	retl 0x88
	retl 0x06
	retl 0x8e
	retl 0x06
	retl 0x95
	retl 0x06
	retl 0x9b
	retl 0x06
	retl 0xa1
	retl 0x06
	retl 0xa7
	retl 0x06
	retl 0xad
	retl 0x06
	retl 0xb4
	retl 0x06
	retl 0xba
	retl 0x06
	retl 0xc0
	retl 0x06
	retl 0xc6
	retl 0x06
	retl 0xcc
	retl 0x06
	retl 0xd3
	retl 0x06
	retl 0xd9
	retl 0x06
	retl 0xdf
	retl 0x06
	retl 0xe5
	retl 0x06
	retl 0xeb
	retl 0x06
	retl 0xf2
	retl 0x06
	retl 0xf8
	retl 0x06
	retl 0xfe
	retl 0x06
	retl 0x04
	retl 0x07
	retl 0x0a
	retl 0x07
	retl 0x11
	retl 0x07
	retl 0x17
	retl 0x07
	retl 0x1d
	retl 0x07
	retl 0x23
	retl 0x07
	retl 0x29
	retl 0x07
	retl 0x30
	retl 0x07
	retl 0x36
	retl 0x07
	retl 0x3c
	retl 0x07
	retl 0x42
	retl 0x07
	retl 0x48
	retl 0x07
	retl 0x4f
	retl 0x07
	retl 0x55
	retl 0x07
	retl 0x5b
	retl 0x07
	retl 0x61
	retl 0x07
	retl 0x67
	retl 0x07
	retl 0x6e
	retl 0x07
	retl 0x74
	retl 0x07
	retl 0x7a
	retl 0x07
	retl 0x80
	retl 0x07
	retl 0x86
	retl 0x07
	retl 0x8d
	retl 0x07
	retl 0x93
	retl 0x07
	retl 0x99
	retl 0x07
	retl 0x9f
	retl 0x07
	retl 0xa5
	retl 0x07
	retl 0xac
	retl 0x07
	retl 0xb2
	retl 0x07
	retl 0xb8
	retl 0x07
	retl 0xbe
	retl 0x07
	retl 0xc4
	retl 0x07
	retl 0xcb
	retl 0x07
	retl 0xd1
	retl 0x07
	retl 0xd7
	retl 0x07
	retl 0xdd
	retl 0x07
	retl 0xe3
	retl 0x07
	retl 0xea
	retl 0x07
	retl 0xf0
	retl 0x07
	retl 0xf6
	retl 0x07
	retl 0xfc
	retl 0x07
	retl 0x02
	retl 0x08
	retl 0x09
	retl 0x08
	retl 0x0f
	retl 0x08
	retl 0x15
	retl 0x08
	retl 0x1b
	retl 0x08
	retl 0x21
	retl 0x08
	retl 0x28
	retl 0x08
	retl 0x2e
	retl 0x08
	retl 0x34
	retl 0x08
	retl 0x3a
	retl 0x08
	retl 0x43
	retl 0x08
	retl 0x47
	retl 0x08


;@Allocation info for local variables in function 'sw_adcBatVal'
;@sw_adcBatVal ADC_GetValue              Allocated to registers ;size:2
;@sw_adcBatVal RSRbits                   Allocated to registers ;size:1
;@sw_adcBatVal PCHbits                   Allocated to registers ;size:1
;@sw_adcBatVal PCLbits                   Allocated to registers ;size:1
;@sw_adcBatVal STATUSbits                Allocated to registers ;size:1
;@sw_adcBatVal TC0CONbits                Allocated to registers ;size:1
;@sw_adcBatVal TC0Cbits                  Allocated to registers ;size:1
;@sw_adcBatVal TBRDHbits                 Allocated to registers ;size:1
;@sw_adcBatVal TBRDLbits                 Allocated to registers ;size:1
;@sw_adcBatVal CPUCONbits                Allocated to registers ;size:1
;@sw_adcBatVal IHRCCALbits               Allocated to registers ;size:1
;@sw_adcBatVal PORT5bits                 Allocated to registers ;size:1
;@sw_adcBatVal PORT6bits                 Allocated to registers ;size:1
;@sw_adcBatVal P5CONbits                 Allocated to registers ;size:1
;@sw_adcBatVal P6CONbits                 Allocated to registers ;size:1
;@sw_adcBatVal P5PHbits                  Allocated to registers ;size:1
;@sw_adcBatVal P6PHbits                  Allocated to registers ;size:1
;@sw_adcBatVal P5PDbits                  Allocated to registers ;size:1
;@sw_adcBatVal P6PDbits                  Allocated to registers ;size:1
;@sw_adcBatVal P6ODbits                  Allocated to registers ;size:1
;@sw_adcBatVal P6WDbits                  Allocated to registers ;size:1
;@sw_adcBatVal P5IWEbits                 Allocated to registers ;size:1
;@sw_adcBatVal P6IWEbits                 Allocated to registers ;size:1
;@sw_adcBatVal P5ADEbits                 Allocated to registers ;size:1
;@sw_adcBatVal P6ADEbits                 Allocated to registers ;size:1
;@sw_adcBatVal ADATHbits                 Allocated to registers ;size:1
;@sw_adcBatVal ADATLbits                 Allocated to registers ;size:1
;@sw_adcBatVal ADISbits                  Allocated to registers ;size:1
;@sw_adcBatVal ADCON0bits                Allocated to registers ;size:1
;@sw_adcBatVal ADCON1bits                Allocated to registers ;size:1
;@sw_adcBatVal WDTCONbits                Allocated to registers ;size:1
;@sw_adcBatVal TC1CONbits                Allocated to registers ;size:1
;@sw_adcBatVal TC1PRDLbits               Allocated to registers ;size:1
;@sw_adcBatVal PWM1DTLbits               Allocated to registers ;size:1
;@sw_adcBatVal TC1PRDTHbits              Allocated to registers ;size:1
;@sw_adcBatVal TC1CHbits                 Allocated to registers ;size:1
;@sw_adcBatVal TC1CLbits                 Allocated to registers ;size:1
;@sw_adcBatVal TC2CONbits                Allocated to registers ;size:1
;@sw_adcBatVal TC2PRDLbits               Allocated to registers ;size:1
;@sw_adcBatVal PWM2DTLbits               Allocated to registers ;size:1
;@sw_adcBatVal TC2PRDTHbits              Allocated to registers ;size:1
;@sw_adcBatVal TC2CHbits                 Allocated to registers ;size:1
;@sw_adcBatVal TC2CLbits                 Allocated to registers ;size:1
;@sw_adcBatVal PWM3DTHbits               Allocated to registers ;size:1
;@sw_adcBatVal PWM3DTLbits               Allocated to registers ;size:1
;@sw_adcBatVal PWM4DTHbits               Allocated to registers ;size:1
;@sw_adcBatVal PWM4DTLbits               Allocated to registers ;size:1
;@sw_adcBatVal PWMISbits                 Allocated to registers ;size:1
;@sw_adcBatVal DEADCONbits               Allocated to registers ;size:1
;@sw_adcBatVal PWMCONbits                Allocated to registers ;size:1
;@sw_adcBatVal DEADT0bits                Allocated to registers ;size:1
;@sw_adcBatVal DEADT1bits                Allocated to registers ;size:1
;@sw_adcBatVal INTE0bits                 Allocated to registers ;size:1
;@sw_adcBatVal INTE1bits                 Allocated to registers ;size:1
;@sw_adcBatVal INTF0bits                 Allocated to registers ;size:1
;@sw_adcBatVal INTF1bits                 Allocated to registers ;size:1
;@sw_adcBatVal IARbits                   Allocated to registers ;size:1
;@sw_adcBatVal U_Flage1                  Allocated to registers ;size:1
;@sw_adcBatVal r_g_workMod               Allocated to registers ;size:1
;@sw_adcBatVal r_g_batVal                Allocated to registers ;size:1
;@sw_adcBatVal r_gbatvalsum              Allocated to registers ;size:2
;@sw_adcBatVal r_gbatvalcnt              Allocated to registers ;size:1
;@sw_adcBatVal r_buff                    Allocated to registers ;size:1
;@sw_adcBatVal adcValue                  Allocated to registers ;size:2
;@sw_adcBatVal r_g_batValChangeCnt       Allocated to registers ;size:1
;@sw_adcBatVal r_g_batValAddCnt          Allocated to registers ;size:1
;@sw_adcBatVal r_g_batValDecCnt          Allocated to registers ;size:1
;@sw_adcBatVal r_g_batValAddShk          Allocated to registers ;size:2
;@sw_adcBatVal r_g_batValDecShk          Allocated to registers ;size:2
;@sw_adcBatVal r_g_batValChangeShkSet    Allocated to registers ;size:2
;@sw_adcBatVal left                      Allocated to registers r0x1012 ;size:1
;@sw_adcBatVal right                     Allocated to registers r0x1013 ;size:1
;@sw_adcBatVal median                    Allocated to registers r0x1014 ;size:1
;@sw_adcBatVal RSR                       Allocated to registers ;size:1
;@sw_adcBatVal PCH                       Allocated to registers ;size:1
;@sw_adcBatVal PCL                       Allocated to registers ;size:1
;@sw_adcBatVal STATUS                    Allocated to registers ;size:1
;@sw_adcBatVal TC0CON                    Allocated to registers ;size:1
;@sw_adcBatVal TC0C                      Allocated to registers ;size:1
;@sw_adcBatVal TBRDH                     Allocated to registers ;size:1
;@sw_adcBatVal TBRDL                     Allocated to registers ;size:1
;@sw_adcBatVal CPUCON                    Allocated to registers ;size:1
;@sw_adcBatVal IHRCCAL                   Allocated to registers ;size:1
;@sw_adcBatVal PORT5                     Allocated to registers ;size:1
;@sw_adcBatVal PORT6                     Allocated to registers ;size:1
;@sw_adcBatVal P5CON                     Allocated to registers ;size:1
;@sw_adcBatVal P6CON                     Allocated to registers ;size:1
;@sw_adcBatVal P5PH                      Allocated to registers ;size:1
;@sw_adcBatVal P6PH                      Allocated to registers ;size:1
;@sw_adcBatVal P5PD                      Allocated to registers ;size:1
;@sw_adcBatVal P6PD                      Allocated to registers ;size:1
;@sw_adcBatVal P6OD                      Allocated to registers ;size:1
;@sw_adcBatVal P6WD                      Allocated to registers ;size:1
;@sw_adcBatVal P5IWE                     Allocated to registers ;size:1
;@sw_adcBatVal P6IWE                     Allocated to registers ;size:1
;@sw_adcBatVal P5ADE                     Allocated to registers ;size:1
;@sw_adcBatVal P6ADE                     Allocated to registers ;size:1
;@sw_adcBatVal ADATH                     Allocated to registers ;size:1
;@sw_adcBatVal ADATL                     Allocated to registers ;size:1
;@sw_adcBatVal ADIS                      Allocated to registers ;size:1
;@sw_adcBatVal ADCON0                    Allocated to registers ;size:1
;@sw_adcBatVal ADCON1                    Allocated to registers ;size:1
;@sw_adcBatVal WDTCON                    Allocated to registers ;size:1
;@sw_adcBatVal TC1CON                    Allocated to registers ;size:1
;@sw_adcBatVal TC1PRDL                   Allocated to registers ;size:1
;@sw_adcBatVal PWM1DTL                   Allocated to registers ;size:1
;@sw_adcBatVal TC1PRDTH                  Allocated to registers ;size:1
;@sw_adcBatVal TC1CH                     Allocated to registers ;size:1
;@sw_adcBatVal TC1CL                     Allocated to registers ;size:1
;@sw_adcBatVal TC2CON                    Allocated to registers ;size:1
;@sw_adcBatVal TC2PRDL                   Allocated to registers ;size:1
;@sw_adcBatVal PWM2DTL                   Allocated to registers ;size:1
;@sw_adcBatVal TC2PRDTH                  Allocated to registers ;size:1
;@sw_adcBatVal TC2CH                     Allocated to registers ;size:1
;@sw_adcBatVal TC2CL                     Allocated to registers ;size:1
;@sw_adcBatVal PWM3DTH                   Allocated to registers ;size:1
;@sw_adcBatVal PWM3DTL                   Allocated to registers ;size:1
;@sw_adcBatVal PWM4DTH                   Allocated to registers ;size:1
;@sw_adcBatVal PWM4DTL                   Allocated to registers ;size:1
;@sw_adcBatVal PWMIS                     Allocated to registers ;size:1
;@sw_adcBatVal DEADCON                   Allocated to registers ;size:1
;@sw_adcBatVal PWMCON                    Allocated to registers ;size:1
;@sw_adcBatVal DEADT0                    Allocated to registers ;size:1
;@sw_adcBatVal DEADT1                    Allocated to registers ;size:1
;@sw_adcBatVal INTE0                     Allocated to registers ;size:1
;@sw_adcBatVal INTE1                     Allocated to registers ;size:1
;@sw_adcBatVal INTF0                     Allocated to registers ;size:1
;@sw_adcBatVal INTF1                     Allocated to registers ;size:1
;@sw_adcBatVal IAR                       Allocated to registers ;size:1
;@end Allocation info for local variables in function 'sw_adcBatVal';

;--------------------------------------------------------
; overlayable items in internal ram 
;--------------------------------------------------------
;	udata_ovr
;--------------------------------------------------------
; code
;--------------------------------------------------------
code_BAT	code
;***
;  pBlock Stats: dbName = C
;***
;has an exit
;functions called:
;   _ADC_GetValue
;   __mulchar
;   (_t_tabBatValTab + 0)
;   (_t_tabBatValTab + 0)
;   _ADC_GetValue
;   __mulchar
;   (_t_tabBatValTab + 0)
;   (_t_tabBatValTab + 0)
;8 compiler assigned registers:
;   r0x1012
;   r0x1013
;   STK00
;   r0x1014
;   r0x1015
;   r0x1016
;   r0x1017
;   r0x1018
;; Starting pCode block
S_BAT__sw_adcBatVal	code
_sw_adcBatVal:	;Function start
; 2 exit points
;	.line	137; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	uint8_t left = 0;          // 查找范围左边界
	CLR	r0x1012
;	.line	138; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	uint8_t right = 101;       // 查找范围右边界
	MOV	A,@0x65
	MOV	r0x1013,A
;	.line	142; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	adcValue = ADC_GetValue(E_AD14, E_Vrefh_1_5V);
	MOV	A,@0x04
	MOV	STK00,A
	MOV	A,@0x0e
	CALL	_ADC_GetValue
	MOV	(_adcValue + 1),A
	MOV	A,STK00
	MOV	_adcValue,A
_00111_DS_:
;	.line	149; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	median = left + right;
	MOV	A,r0x1013
	ADD	A,r0x1012
	MOV	r0x1014,A
;	.line	150; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	median = median >> 1;
	BTC	STATUS,0
	RCR	r0x1014
;	.line	153; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	if (left == median)
	MOV	A,r0x1014
	XOR	A,r0x1012
	JBTS	STATUS,2
	JMP	_00264_DS_
	JMP	_00112_DS_
_00264_DS_:
;	.line	159; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	if (adcValue < t_tabBatValTab[median])
	MOV	A,@0x02
	MOV	STK00,A
	MOV	A,r0x1014
	CALL	__mulchar
	MOV	r0x1015,A
;;1	CLR	r0x1016
	MOV	A,r0x1015
	CALL	(_t_tabBatValTab + 0)
	MOV	r0x1017,A
	IJA	r0x1015
	CALL	(_t_tabBatValTab + 0)
	MOV	r0x1018,A
	MOV	A,r0x1018
	SUB	A,(_adcValue + 1)
	JBTS	STATUS,2
	JMP	_00265_DS_
	MOV	A,r0x1017
	SUB	A,_adcValue
_00265_DS_:
	JBTC	STATUS,0
	JMP	_00108_DS_
;	.line	161; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	right = median;    // 目标值在左半部分
	MOV	A,r0x1014
	MOV	r0x1013,A
	JMP	_00111_DS_
_00108_DS_:
;	.line	165; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	left = median;     // 目标值在右半部分
	MOV	A,r0x1014
	MOV	r0x1012,A
	JMP	_00111_DS_
_00112_DS_:
;	.line	168; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	if(r_gbatvalcnt == 0)
	MOV	A,@0x00
	OR	A,_r_gbatvalcnt
	JBTS	STATUS,2
	JMP	_00114_DS_
;	.line	170; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_gbatvalsum = 0;
	CLR	_r_gbatvalsum
	CLR	(_r_gbatvalsum + 1)
_00114_DS_:
;	.line	173; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	median = 100 - median;
	MOV	A,r0x1014
	SUB	A,@0x64
	MOV	r0x1014,A
;	.line	174; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_gbatvalsum += median;
	MOV	A,r0x1014
	MOV	r0x1014,A
	MOV	r0x1012,A
	CLR	r0x1013
;;99	MOV	A,r0x1012
;;103	MOV	A,r0x1013
	MOV	A,r0x1014
	ADD	_r_gbatvalsum,A
;;102	MOV	A,r0x1015
	MOV	A,@0x00
	MOV	r0x1015,A
	MOV	A,r0x1015
	JBTC	STATUS,0
	IJA	r0x1015
	ADD	(_r_gbatvalsum + 1),A
;	.line	176; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	if(++r_gbatvalcnt >= 16)
	INC	_r_gbatvalcnt
	MOV	A,@0x10
	SUB	A,_r_gbatvalcnt
	JBTS	STATUS,0
	JMP	_00172_DS_
;	.line	178; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_gbatvalcnt = 0;
	CLR	_r_gbatvalcnt
;	.line	180; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_gbatvalsum += 8;
	MOV	A,@0x08
	ADD	_r_gbatvalsum,A
	JBTC	STATUS,0
	INC	(_r_gbatvalsum + 1)
;	.line	181; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_gbatvalsum = r_gbatvalsum >> 4; // 平均值
	SWAPA	_r_gbatvalsum
	AND	A,@0x0f
	MOV	_r_gbatvalsum,A
	SWAPA	(_r_gbatvalsum + 1)
	MOV	(_r_gbatvalsum + 1),A
	AND	A,@0xf0
	OR	_r_gbatvalsum,A
	XOR	(_r_gbatvalsum + 1),A
;;swapping arguments (AOP_TYPEs 1/3)
;	.line	182; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	if (r_gbatvalsum > D_CHECK_BAT_VAL_NUM)
	MOV	A,@0x00
	SUB	A,(_r_gbatvalsum + 1)
	JBTS	STATUS,2
	JMP	_00267_DS_
	MOV	A,@0x65
	SUB	A,_r_gbatvalsum
_00267_DS_:
	JBTS	STATUS,0
	JMP	_00116_DS_
;	.line	184; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_gbatvalsum = D_CHECK_BAT_VAL_NUM;
	MOV	A,@0x64
	MOV	_r_gbatvalsum,A
	CLR	(_r_gbatvalsum + 1)
_00116_DS_:
;	.line	187; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	if(F_FIRST_POWER_UP == 1 )
	CLR	r0x1012
	JBTC	_U_Flage1,6
	INC	r0x1012
;;109	MOV	A,r0x1012
;;108	MOV	A,r0x1013
	MOV	A,r0x1012
	MOV	r0x1013,A
	XOR	A,@0x01
	JBTS	STATUS,2
	JMP	_00168_DS_
;	.line	189; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	F_FIRST_POWER_UP = 0;
	BTC	_U_Flage1,6
;	.line	190; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_buff = r_gbatvalsum;
	MOV	A,_r_gbatvalsum
	MOV	_r_buff,A
;	.line	191; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_g_batVal = r_buff;            // 返回找到的电量百分比
	MOV	A,_r_buff
	MOV	_r_g_batVal,A
	JMP	_00172_DS_
_00168_DS_:
;	.line	193; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	else if(F_CHARGE == 1 || r_g_workMod)
	CLR	r0x1012
	JBTC	_U_Flage1,4
	INC	r0x1012
;;107	MOV	A,r0x1012
;;106	MOV	A,r0x1013
	MOV	A,r0x1012
	MOV	r0x1013,A
	XOR	A,@0x01
	JBTS	STATUS,2
	JMP	_00268_DS_
	JMP	_00164_DS_
_00268_DS_:
	MOV	A,@0x00
	OR	A,_r_g_workMod
	JBTC	STATUS,2
	JMP	_00172_DS_
_00164_DS_:
;	.line	197; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	if(++r_g_batValChangeCnt <= D_BAT_VAL_CNT_SHK)
	INC	_r_g_batValChangeCnt
;;swapping arguments (AOP_TYPEs 1/3)
	MOV	A,@0x1f
	SUB	A,_r_g_batValChangeCnt
	JBTC	STATUS,0
	JMP	_00131_DS_
;	.line	199; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	if(r_gbatvalsum > r_buff)
	MOV	A,_r_buff
	MOV	r0x1012,A
	CLR	r0x1013
	MOV	A,(_r_gbatvalsum + 1)
	SUB	A,r0x1013
	JBTS	STATUS,2
	JMP	_00270_DS_
	MOV	A,_r_gbatvalsum
	SUB	A,r0x1012
_00270_DS_:
	JBTC	STATUS,0
	JMP	_00120_DS_
;	.line	201; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_g_batValAddCnt++;
	INC	_r_g_batValAddCnt
	JMP	_00132_DS_
_00120_DS_:
;	.line	203; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	else if(r_gbatvalsum < r_buff)
	MOV	A,r0x1013
	SUB	A,(_r_gbatvalsum + 1)
	JBTS	STATUS,2
	JMP	_00271_DS_
	MOV	A,r0x1012
	SUB	A,_r_gbatvalsum
_00271_DS_:
	JBTC	STATUS,0
	JMP	_00132_DS_
;	.line	205; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_g_batValDecCnt++;
	INC	_r_g_batValDecCnt
	JMP	_00132_DS_
;;swapping arguments (AOP_TYPEs 1/3)
_00131_DS_:
;	.line	211; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	if(r_g_batValAddCnt > D_BAT_VAL_ADD_SHK && F_CHARGE == ENABLE)
	MOV	A,@0x1a
	SUB	A,_r_g_batValAddCnt
	JBTS	STATUS,0
	JMP	_00127_DS_
	CLR	r0x1012
	JBTC	_U_Flage1,4
	INC	r0x1012
;;105	MOV	A,r0x1012
;;104	MOV	A,r0x1013
	MOV	A,r0x1012
	MOV	r0x1013,A
	XOR	A,@0x01
	JBTS	STATUS,2
	JMP	_00127_DS_
;	.line	213; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_buff = r_gbatvalsum;
	MOV	A,_r_gbatvalsum
	MOV	_r_buff,A
	JMP	_00128_DS_
;;swapping arguments (AOP_TYPEs 1/3)
_00127_DS_:
;	.line	215; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	else if(r_g_batValDecCnt > D_BAT_VAL_DEC_SHK&& F_CHARGE == DISABLE && r_g_workMod)
	MOV	A,@0x1a
	SUB	A,_r_g_batValDecCnt
	JBTS	STATUS,0
	JMP	_00128_DS_
	JBTC	_U_Flage1,4
	JMP	_00128_DS_
	MOV	A,@0x00
	OR	A,_r_g_workMod
	JBTC	STATUS,2
	JMP	_00128_DS_
;	.line	217; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_buff = r_gbatvalsum;
	MOV	A,_r_gbatvalsum
	MOV	_r_buff,A
_00128_DS_:
;	.line	219; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_g_batValChangeCnt = 0;
	CLR	_r_g_batValChangeCnt
;	.line	220; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_g_batValDecCnt = 0;
	CLR	_r_g_batValDecCnt
;	.line	221; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_g_batValAddCnt = 0;
	CLR	_r_g_batValAddCnt
_00132_DS_:
;	.line	223; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	if(F_CHARGE == ENABLE)
	CLR	r0x1012
	JBTC	_U_Flage1,4
	INC	r0x1012
;;101	MOV	A,r0x1012
;;100	MOV	A,r0x1013
	MOV	A,r0x1012
	MOV	r0x1013,A
	XOR	A,@0x01
	JBTS	STATUS,2
	JMP	_00139_DS_
;	.line	225; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_g_batValChangeShkSet = 100; //7.5s
	MOV	A,@0x64
	MOV	_r_g_batValChangeShkSet,A
	CLR	(_r_g_batValChangeShkSet + 1)
	JMP	_00140_DS_
_00139_DS_:
;	.line	227; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	else if(r_g_workMod)
	MOV	A,@0x00
	OR	A,_r_g_workMod
	JBTC	STATUS,2
	JMP	_00140_DS_
;	.line	229; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	if(r_buff < 10)
	MOV	A,@0x0a
	SUB	A,_r_buff
	JBTC	STATUS,0
	JMP	_00134_DS_
;	.line	231; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_g_batValChangeShkSet = 40;
	MOV	A,@0x28
	MOV	_r_g_batValChangeShkSet,A
	CLR	(_r_g_batValChangeShkSet + 1)
	JMP	_00140_DS_
_00134_DS_:
;	.line	235; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_g_batValChangeShkSet = 100;
	MOV	A,@0x64
	MOV	_r_g_batValChangeShkSet,A
	CLR	(_r_g_batValChangeShkSet + 1)
_00140_DS_:
;	.line	238; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	if(F_CHARGE)
	JBTS	_U_Flage1,4
	JMP	_00158_DS_
;	.line	240; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_g_batValDecShk = 0; //放电计时清零
	CLR	_r_g_batValDecShk
	CLR	(_r_g_batValDecShk + 1)
;	.line	241; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	if(F_CHARGE_FULL || r_buff > r_g_batVal)
	JBTC	_U_Flage1,5
	JMP	_00145_DS_
	MOV	A,_r_buff
	SUB	A,_r_g_batVal
	JBTC	STATUS,0
	JMP	_00159_DS_
_00145_DS_:
;	.line	243; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	if(++r_g_batValAddShk >= r_g_batValChangeShkSet)
	INC	_r_g_batValAddShk
	JBTC	STATUS,2
	INC	(_r_g_batValAddShk + 1)
	MOV	A,(_r_g_batValChangeShkSet + 1)
	SUB	A,(_r_g_batValAddShk + 1)
	JBTS	STATUS,2
	JMP	_00276_DS_
	MOV	A,_r_g_batValChangeShkSet
	SUB	A,_r_g_batValAddShk
_00276_DS_:
	JBTS	STATUS,0
	JMP	_00159_DS_
;	.line	245; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_g_batValAddShk = 0;
	CLR	_r_g_batValAddShk
	CLR	(_r_g_batValAddShk + 1)
;	.line	246; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	if(r_g_batVal < 100)
	MOV	A,@0x64
	SUB	A,_r_g_batVal
	JBTC	STATUS,0
	JMP	_00159_DS_
;	.line	248; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_g_batVal++;
	INC	_r_g_batVal
	JMP	_00159_DS_
_00158_DS_:
;	.line	253; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	else if(r_g_workMod)
	MOV	A,@0x00
	OR	A,_r_g_workMod
	JBTC	STATUS,2
	JMP	_00155_DS_
;	.line	255; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_g_batValAddShk = 0; //充电计时清零
	CLR	_r_g_batValAddShk
	CLR	(_r_g_batValAddShk + 1)
;	.line	256; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	if(r_buff < r_g_batVal)
	MOV	A,_r_g_batVal
	SUB	A,_r_buff
	JBTC	STATUS,0
	JMP	_00159_DS_
;	.line	258; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	if(++r_g_batValDecShk >= r_g_batValChangeShkSet)
	INC	_r_g_batValDecShk
	JBTC	STATUS,2
	INC	(_r_g_batValDecShk + 1)
	MOV	A,(_r_g_batValChangeShkSet + 1)
	SUB	A,(_r_g_batValDecShk + 1)
	JBTS	STATUS,2
	JMP	_00279_DS_
	MOV	A,_r_g_batValChangeShkSet
	SUB	A,_r_g_batValDecShk
_00279_DS_:
	JBTS	STATUS,0
	JMP	_00159_DS_
;	.line	260; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_g_batValDecShk = 0;
	CLR	_r_g_batValDecShk
	CLR	(_r_g_batValDecShk + 1)
;	.line	261; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	if(r_g_batVal > 0)
	MOV	A,@0x00
	OR	A,_r_g_batVal
	JBTC	STATUS,2
	JMP	_00159_DS_
;	.line	263; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_g_batVal--;
	DEC	_r_g_batVal
	JMP	_00159_DS_
_00155_DS_:
;	.line	270; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_g_batValAddShk = 0;
	CLR	_r_g_batValAddShk
	CLR	(_r_g_batValAddShk + 1)
;	.line	271; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_g_batValDecShk = 0;
	CLR	_r_g_batValDecShk
	CLR	(_r_g_batValDecShk + 1)
_00159_DS_:
;	.line	273; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	if (r_g_workMod != DISABLE && r_buff == 0 && F_CHARGE == DISABLE)
	MOV	A,@0x00
	OR	A,_r_g_workMod
	JBTC	STATUS,2
	JMP	_00172_DS_
	MOV	A,@0x00
	OR	A,_r_buff
	JBTS	STATUS,2
	JMP	_00172_DS_
	JBTC	_U_Flage1,4
	JMP	_00172_DS_
;	.line	275; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_g_workMod = 0;
	CLR	_r_g_workMod
;	.line	276; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	r_g_batVal = 0;
	CLR	_r_g_batVal
;	.line	286; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\BAT.C	}
_00172_DS_:
	RET	
; exit point of _sw_adcBatVal


;	code size estimation:
;	  282+    0 =   282 instructions (  564 byte)

	end
