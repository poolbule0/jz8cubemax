;--------------------------------------------------------
; File Created by SLCC : free open source ANSI-C Compiler
; Version 3.6.0 #Sep 28 2025 (MSVC)
;--------------------------------------------------------
; SL port for the RISC core
;--------------------------------------------------------
;	.file	"C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\KEY.C"
	list	p=JZ8P2615
	radix dec
	include "JZ8P2615.inc"
;--------------------------------------------------------
; external declarations
;--------------------------------------------------------
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
	global	_key_scan
	global	_key_cnt
	global	_key_press
	global	_flag

;--------------------------------------------------------
; global definitions
;--------------------------------------------------------
UD_KEY_0	udata
_key_cnt	res	1

UD_KEY_1	udata
_key_press	res	1

UD_KEY_2	udata
_flag	res	1

;--------------------------------------------------------
; absolute symbol definitions
;--------------------------------------------------------
;--------------------------------------------------------
; compiler-defined variables
;--------------------------------------------------------
UDL_KEY_0	udata
r0x1003	res	1
r0x1004	res	1
;--------------------------------------------------------
; initialized data
;--------------------------------------------------------

;@Allocation info for local variables in function 'key_scan'
;@key_scan RSRbits                   Allocated to registers ;size:1
;@key_scan PCHbits                   Allocated to registers ;size:1
;@key_scan PCLbits                   Allocated to registers ;size:1
;@key_scan STATUSbits                Allocated to registers ;size:1
;@key_scan TC0CONbits                Allocated to registers ;size:1
;@key_scan TC0Cbits                  Allocated to registers ;size:1
;@key_scan TBRDHbits                 Allocated to registers ;size:1
;@key_scan TBRDLbits                 Allocated to registers ;size:1
;@key_scan CPUCONbits                Allocated to registers ;size:1
;@key_scan IHRCCALbits               Allocated to registers ;size:1
;@key_scan PORT5bits                 Allocated to registers ;size:1
;@key_scan PORT6bits                 Allocated to registers ;size:1
;@key_scan P5CONbits                 Allocated to registers ;size:1
;@key_scan P6CONbits                 Allocated to registers ;size:1
;@key_scan P5PHbits                  Allocated to registers ;size:1
;@key_scan P6PHbits                  Allocated to registers ;size:1
;@key_scan P5PDbits                  Allocated to registers ;size:1
;@key_scan P6PDbits                  Allocated to registers ;size:1
;@key_scan P6ODbits                  Allocated to registers ;size:1
;@key_scan P6WDbits                  Allocated to registers ;size:1
;@key_scan P5IWEbits                 Allocated to registers ;size:1
;@key_scan P6IWEbits                 Allocated to registers ;size:1
;@key_scan P5ADEbits                 Allocated to registers ;size:1
;@key_scan P6ADEbits                 Allocated to registers ;size:1
;@key_scan ADATHbits                 Allocated to registers ;size:1
;@key_scan ADATLbits                 Allocated to registers ;size:1
;@key_scan ADISbits                  Allocated to registers ;size:1
;@key_scan ADCON0bits                Allocated to registers ;size:1
;@key_scan ADCON1bits                Allocated to registers ;size:1
;@key_scan WDTCONbits                Allocated to registers ;size:1
;@key_scan TC1CONbits                Allocated to registers ;size:1
;@key_scan TC1PRDLbits               Allocated to registers ;size:1
;@key_scan PWM1DTLbits               Allocated to registers ;size:1
;@key_scan TC1PRDTHbits              Allocated to registers ;size:1
;@key_scan TC1CHbits                 Allocated to registers ;size:1
;@key_scan TC1CLbits                 Allocated to registers ;size:1
;@key_scan TC2CONbits                Allocated to registers ;size:1
;@key_scan TC2PRDLbits               Allocated to registers ;size:1
;@key_scan PWM2DTLbits               Allocated to registers ;size:1
;@key_scan TC2PRDTHbits              Allocated to registers ;size:1
;@key_scan TC2CHbits                 Allocated to registers ;size:1
;@key_scan TC2CLbits                 Allocated to registers ;size:1
;@key_scan PWM3DTHbits               Allocated to registers ;size:1
;@key_scan PWM3DTLbits               Allocated to registers ;size:1
;@key_scan PWM4DTHbits               Allocated to registers ;size:1
;@key_scan PWM4DTLbits               Allocated to registers ;size:1
;@key_scan PWMISbits                 Allocated to registers ;size:1
;@key_scan DEADCONbits               Allocated to registers ;size:1
;@key_scan PWMCONbits                Allocated to registers ;size:1
;@key_scan DEADT0bits                Allocated to registers ;size:1
;@key_scan DEADT1bits                Allocated to registers ;size:1
;@key_scan INTE0bits                 Allocated to registers ;size:1
;@key_scan INTE1bits                 Allocated to registers ;size:1
;@key_scan INTF0bits                 Allocated to registers ;size:1
;@key_scan INTF1bits                 Allocated to registers ;size:1
;@key_scan IARbits                   Allocated to registers ;size:1
;@key_scan U_Flage1                  Allocated to registers ;size:1
;@key_scan r_g_workMod               Allocated to registers ;size:1
;@key_scan key_cnt                   Allocated to registers ;size:1
;@key_scan key_press                 Allocated to registers ;size:1
;@key_scan flag                      Allocated to registers ;size:1
;@key_scan RSR                       Allocated to registers ;size:1
;@key_scan PCH                       Allocated to registers ;size:1
;@key_scan PCL                       Allocated to registers ;size:1
;@key_scan STATUS                    Allocated to registers ;size:1
;@key_scan TC0CON                    Allocated to registers ;size:1
;@key_scan TC0C                      Allocated to registers ;size:1
;@key_scan TBRDH                     Allocated to registers ;size:1
;@key_scan TBRDL                     Allocated to registers ;size:1
;@key_scan CPUCON                    Allocated to registers ;size:1
;@key_scan IHRCCAL                   Allocated to registers ;size:1
;@key_scan PORT5                     Allocated to registers ;size:1
;@key_scan PORT6                     Allocated to registers ;size:1
;@key_scan P5CON                     Allocated to registers ;size:1
;@key_scan P6CON                     Allocated to registers ;size:1
;@key_scan P5PH                      Allocated to registers ;size:1
;@key_scan P6PH                      Allocated to registers ;size:1
;@key_scan P5PD                      Allocated to registers ;size:1
;@key_scan P6PD                      Allocated to registers ;size:1
;@key_scan P6OD                      Allocated to registers ;size:1
;@key_scan P6WD                      Allocated to registers ;size:1
;@key_scan P5IWE                     Allocated to registers ;size:1
;@key_scan P6IWE                     Allocated to registers ;size:1
;@key_scan P5ADE                     Allocated to registers ;size:1
;@key_scan P6ADE                     Allocated to registers ;size:1
;@key_scan ADATH                     Allocated to registers ;size:1
;@key_scan ADATL                     Allocated to registers ;size:1
;@key_scan ADIS                      Allocated to registers ;size:1
;@key_scan ADCON0                    Allocated to registers ;size:1
;@key_scan ADCON1                    Allocated to registers ;size:1
;@key_scan WDTCON                    Allocated to registers ;size:1
;@key_scan TC1CON                    Allocated to registers ;size:1
;@key_scan TC1PRDL                   Allocated to registers ;size:1
;@key_scan PWM1DTL                   Allocated to registers ;size:1
;@key_scan TC1PRDTH                  Allocated to registers ;size:1
;@key_scan TC1CH                     Allocated to registers ;size:1
;@key_scan TC1CL                     Allocated to registers ;size:1
;@key_scan TC2CON                    Allocated to registers ;size:1
;@key_scan TC2PRDL                   Allocated to registers ;size:1
;@key_scan PWM2DTL                   Allocated to registers ;size:1
;@key_scan TC2PRDTH                  Allocated to registers ;size:1
;@key_scan TC2CH                     Allocated to registers ;size:1
;@key_scan TC2CL                     Allocated to registers ;size:1
;@key_scan PWM3DTH                   Allocated to registers ;size:1
;@key_scan PWM3DTL                   Allocated to registers ;size:1
;@key_scan PWM4DTH                   Allocated to registers ;size:1
;@key_scan PWM4DTL                   Allocated to registers ;size:1
;@key_scan PWMIS                     Allocated to registers ;size:1
;@key_scan DEADCON                   Allocated to registers ;size:1
;@key_scan PWMCON                    Allocated to registers ;size:1
;@key_scan DEADT0                    Allocated to registers ;size:1
;@key_scan DEADT1                    Allocated to registers ;size:1
;@key_scan INTE0                     Allocated to registers ;size:1
;@key_scan INTE1                     Allocated to registers ;size:1
;@key_scan INTF0                     Allocated to registers ;size:1
;@key_scan INTF1                     Allocated to registers ;size:1
;@key_scan IAR                       Allocated to registers ;size:1
;@end Allocation info for local variables in function 'key_scan';

;--------------------------------------------------------
; overlayable items in internal ram 
;--------------------------------------------------------
;	udata_ovr
;--------------------------------------------------------
; code
;--------------------------------------------------------
code_KEY	code
;***
;  pBlock Stats: dbName = C
;***
;has an exit
;2 compiler assigned registers:
;   r0x1003
;   r0x1004
;; Starting pCode block
S_KEY__key_scan	code
_key_scan:	;Function start
; 2 exit points
;	.line	11; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\KEY.C	if (Io_Key == 0) // 按下（低电平有效）
	JBTC	_PORT6bits,3
	JMP	_00116_DS_
;	.line	13; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\KEY.C	if (key_press == 0) // 还未确认按下，进行按下去抖
	MOV	A,@0x00
	OR	A,_key_press
	JBTS	STATUS,2
	JMP	_00108_DS_
;	.line	15; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\KEY.C	if (++key_cnt >= 20)
	INC	_key_cnt
	MOV	A,@0x14
	SUB	A,_key_cnt
	JBTS	STATUS,0
	JMP	_00118_DS_
;	.line	17; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\KEY.C	key_cnt = 0;
	CLR	_key_cnt
;	.line	18; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\KEY.C	key_press = 1; // 已确认按下
	MOV	A,@0x01
	MOV	_key_press,A
	JMP	_00118_DS_
_00108_DS_:
;	.line	24; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\KEY.C	key_cnt = 0;
	CLR	_key_cnt
	JMP	_00118_DS_
_00116_DS_:
;	.line	29; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\KEY.C	if (key_press == 1) // 之前处于按下状态，进行松手去抖
	MOV	A,_key_press
	XOR	A,@0x01
	JBTS	STATUS,2
	JMP	_00113_DS_
;	.line	31; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\KEY.C	if (++key_cnt >= 20)
	INC	_key_cnt
	MOV	A,@0x14
	SUB	A,_key_cnt
	JBTS	STATUS,0
	JMP	_00118_DS_
;	.line	33; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\KEY.C	key_cnt = 0;
	CLR	_key_cnt
;	.line	34; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\KEY.C	key_press = 0; // 退出按下状态
	CLR	_key_press
;	.line	37; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\KEY.C	flag ^= 1;
	MOV	A,@0x01
	XOR	_flag,A
;	.line	38; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\KEY.C	Io_Motoer = (flag == 1) ? 1 : 0;
	CLR	r0x1003
	MOV	A,_flag
	XOR	A,@0x01
	JBTS	STATUS,2
	JMP	_00137_DS_
	INC	r0x1003
_00137_DS_:
	MOV	A,r0x1003
	MOV	r0x1004,A
	RCA	r0x1004
	JBTS	STATUS,0
	BTC	_PORT6bits,2
	JBTC	STATUS,0
	BTS	_PORT6bits,2
	JMP	_00118_DS_
_00113_DS_:
;	.line	43; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\KEY.C	key_cnt = 0; // 空闲态
	CLR	_key_cnt
;	.line	46; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\KEY.C	}
_00118_DS_:
	RET	
; exit point of _key_scan


;	code size estimation:
;	   46+    0 =    46 instructions (   92 byte)

	end
