;--------------------------------------------------------
; File Created by SLCC : free open source ANSI-C Compiler
; Version 3.6.0 #Sep 28 2025 (MSVC)
;--------------------------------------------------------
; SL port for the RISC core
;--------------------------------------------------------
;	.file	"C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C"
	list	p=JZ8P2615
	radix dec
	include "JZ8P2615.inc"
;--------------------------------------------------------
; external declarations
;--------------------------------------------------------
	extern	_file_clrRam
	extern	_file_init
	extern	_file_tc0_Init
	extern	_ADC_GetValue
	extern	_sw_adcBatVal
	extern	_SMG_Display
	extern	_SMG_Scan
	extern	_Mode_Check
	extern	_sleep_scan
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
	extern	_r_g_batVal
	extern	_r_buff
	extern	_Flag_Led1
	extern	_Flag_Led2
	extern	_Flag_Led3
	extern	_Flag_Led4
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
;--------------------------------------------------------
; global declarations
;--------------------------------------------------------
	global	_main
	global	_U_Flage1
	global	_r_g_workMod
	global	_led_turn_cnt
	global	_led_turn

	global STK06
	global STK05
	global STK04
	global STK03
	global STK02
	global STK01
	global STK00

sharebank udata_ovr 0x0020
STK06	res 1
STK05	res 1
STK04	res 1
STK03	res 1
STK02	res 1
STK01	res 1
STK00	res 1

;--------------------------------------------------------
; global definitions
;--------------------------------------------------------
UD_MAIN_0	udata
_U_Flage1	res	1

UD_MAIN_1	udata
_r_g_workMod	res	1

UD_MAIN_2	udata
_led_turn_cnt	res	1

UD_MAIN_3	udata
_led_turn	res	1

;--------------------------------------------------------
; absolute symbol definitions
;--------------------------------------------------------
;--------------------------------------------------------
; compiler-defined variables
;--------------------------------------------------------
UDL_MAIN_0	udata
r0x1005	res	1
r0x1006	res	1
;--------------------------------------------------------
; initialized data
;--------------------------------------------------------

;@Allocation info for local variables in function 'main'
;@main file_clrRam               Allocated to registers ;size:2
;@main file_init                 Allocated to registers ;size:2
;@main file_tc0_Init             Allocated to registers ;size:2
;@main ADC_GetValue              Allocated to registers ;size:2
;@main sw_adcBatVal              Allocated to registers ;size:2
;@main SMG_Display               Allocated to registers ;size:2
;@main SMG_Scan                  Allocated to registers ;size:2
;@main Mode_Check                Allocated to registers ;size:2
;@main sleep_scan                Allocated to registers ;size:2
;@main main                      Allocated to registers ;size:2
;@main RSRbits                   Allocated to registers ;size:1
;@main PCHbits                   Allocated to registers ;size:1
;@main PCLbits                   Allocated to registers ;size:1
;@main STATUSbits                Allocated to registers ;size:1
;@main TC0CONbits                Allocated to registers ;size:1
;@main TC0Cbits                  Allocated to registers ;size:1
;@main TBRDHbits                 Allocated to registers ;size:1
;@main TBRDLbits                 Allocated to registers ;size:1
;@main CPUCONbits                Allocated to registers ;size:1
;@main IHRCCALbits               Allocated to registers ;size:1
;@main PORT5bits                 Allocated to registers ;size:1
;@main PORT6bits                 Allocated to registers ;size:1
;@main P5CONbits                 Allocated to registers ;size:1
;@main P6CONbits                 Allocated to registers ;size:1
;@main P5PHbits                  Allocated to registers ;size:1
;@main P6PHbits                  Allocated to registers ;size:1
;@main P5PDbits                  Allocated to registers ;size:1
;@main P6PDbits                  Allocated to registers ;size:1
;@main P6ODbits                  Allocated to registers ;size:1
;@main P6WDbits                  Allocated to registers ;size:1
;@main P5IWEbits                 Allocated to registers ;size:1
;@main P6IWEbits                 Allocated to registers ;size:1
;@main P5ADEbits                 Allocated to registers ;size:1
;@main P6ADEbits                 Allocated to registers ;size:1
;@main ADATHbits                 Allocated to registers ;size:1
;@main ADATLbits                 Allocated to registers ;size:1
;@main ADISbits                  Allocated to registers ;size:1
;@main ADCON0bits                Allocated to registers ;size:1
;@main ADCON1bits                Allocated to registers ;size:1
;@main WDTCONbits                Allocated to registers ;size:1
;@main TC1CONbits                Allocated to registers ;size:1
;@main TC1PRDLbits               Allocated to registers ;size:1
;@main PWM1DTLbits               Allocated to registers ;size:1
;@main TC1PRDTHbits              Allocated to registers ;size:1
;@main TC1CHbits                 Allocated to registers ;size:1
;@main TC1CLbits                 Allocated to registers ;size:1
;@main TC2CONbits                Allocated to registers ;size:1
;@main TC2PRDLbits               Allocated to registers ;size:1
;@main PWM2DTLbits               Allocated to registers ;size:1
;@main TC2PRDTHbits              Allocated to registers ;size:1
;@main TC2CHbits                 Allocated to registers ;size:1
;@main TC2CLbits                 Allocated to registers ;size:1
;@main PWM3DTHbits               Allocated to registers ;size:1
;@main PWM3DTLbits               Allocated to registers ;size:1
;@main PWM4DTHbits               Allocated to registers ;size:1
;@main PWM4DTLbits               Allocated to registers ;size:1
;@main PWMISbits                 Allocated to registers ;size:1
;@main DEADCONbits               Allocated to registers ;size:1
;@main PWMCONbits                Allocated to registers ;size:1
;@main DEADT0bits                Allocated to registers ;size:1
;@main DEADT1bits                Allocated to registers ;size:1
;@main INTE0bits                 Allocated to registers ;size:1
;@main INTE1bits                 Allocated to registers ;size:1
;@main INTF0bits                 Allocated to registers ;size:1
;@main INTF1bits                 Allocated to registers ;size:1
;@main IARbits                   Allocated to registers ;size:1
;@main r_g_batVal                Allocated to registers ;size:1
;@main r_buff                    Allocated to registers ;size:1
;@main Flag_Led1                 Allocated to registers ;size:1
;@main Flag_Led2                 Allocated to registers ;size:1
;@main Flag_Led3                 Allocated to registers ;size:1
;@main Flag_Led4                 Allocated to registers ;size:1
;@main U_Flage1                  Allocated to registers ;size:1
;@main r_g_workMod               Allocated to registers ;size:1
;@main led_turn_cnt              Allocated to registers ;size:1
;@main led_turn                  Allocated to registers ;size:1
;@main RSR                       Allocated to registers ;size:1
;@main PCH                       Allocated to registers ;size:1
;@main PCL                       Allocated to registers ;size:1
;@main STATUS                    Allocated to registers ;size:1
;@main TC0CON                    Allocated to registers ;size:1
;@main TC0C                      Allocated to registers ;size:1
;@main TBRDH                     Allocated to registers ;size:1
;@main TBRDL                     Allocated to registers ;size:1
;@main CPUCON                    Allocated to registers ;size:1
;@main IHRCCAL                   Allocated to registers ;size:1
;@main PORT5                     Allocated to registers ;size:1
;@main PORT6                     Allocated to registers ;size:1
;@main P5CON                     Allocated to registers ;size:1
;@main P6CON                     Allocated to registers ;size:1
;@main P5PH                      Allocated to registers ;size:1
;@main P6PH                      Allocated to registers ;size:1
;@main P5PD                      Allocated to registers ;size:1
;@main P6PD                      Allocated to registers ;size:1
;@main P6OD                      Allocated to registers ;size:1
;@main P6WD                      Allocated to registers ;size:1
;@main P5IWE                     Allocated to registers ;size:1
;@main P6IWE                     Allocated to registers ;size:1
;@main P5ADE                     Allocated to registers ;size:1
;@main P6ADE                     Allocated to registers ;size:1
;@main ADATH                     Allocated to registers ;size:1
;@main ADATL                     Allocated to registers ;size:1
;@main ADIS                      Allocated to registers ;size:1
;@main ADCON0                    Allocated to registers ;size:1
;@main ADCON1                    Allocated to registers ;size:1
;@main WDTCON                    Allocated to registers ;size:1
;@main TC1CON                    Allocated to registers ;size:1
;@main TC1PRDL                   Allocated to registers ;size:1
;@main PWM1DTL                   Allocated to registers ;size:1
;@main TC1PRDTH                  Allocated to registers ;size:1
;@main TC1CH                     Allocated to registers ;size:1
;@main TC1CL                     Allocated to registers ;size:1
;@main TC2CON                    Allocated to registers ;size:1
;@main TC2PRDL                   Allocated to registers ;size:1
;@main PWM2DTL                   Allocated to registers ;size:1
;@main TC2PRDTH                  Allocated to registers ;size:1
;@main TC2CH                     Allocated to registers ;size:1
;@main TC2CL                     Allocated to registers ;size:1
;@main PWM3DTH                   Allocated to registers ;size:1
;@main PWM3DTL                   Allocated to registers ;size:1
;@main PWM4DTH                   Allocated to registers ;size:1
;@main PWM4DTL                   Allocated to registers ;size:1
;@main PWMIS                     Allocated to registers ;size:1
;@main DEADCON                   Allocated to registers ;size:1
;@main PWMCON                    Allocated to registers ;size:1
;@main DEADT0                    Allocated to registers ;size:1
;@main DEADT1                    Allocated to registers ;size:1
;@main INTE0                     Allocated to registers ;size:1
;@main INTE1                     Allocated to registers ;size:1
;@main INTF0                     Allocated to registers ;size:1
;@main INTF1                     Allocated to registers ;size:1
;@main IAR                       Allocated to registers ;size:1
;@end Allocation info for local variables in function 'main';

;--------------------------------------------------------
; overlayable items in internal ram 
;--------------------------------------------------------
;	udata_ovr
;--------------------------------------------------------
; reset vector 
;--------------------------------------------------------
STARTUP	code 0x0000
	jmp	_main
;--------------------------------------------------------
; code
;--------------------------------------------------------
code_MAIN	code
;***
;  pBlock Stats: dbName = M
;***
;has an exit
;functions called:
;   _file_clrRam
;   _file_init
;   _file_tc0_Init
;   _sleep_scan
;   _SMG_Display
;   _SMG_Display
;   _SMG_Display
;   _Mode_Check
;   _sw_adcBatVal
;   _file_clrRam
;   _file_init
;   _file_tc0_Init
;   _sleep_scan
;   _SMG_Display
;   _SMG_Display
;   _SMG_Display
;   _Mode_Check
;   _sw_adcBatVal
;3 compiler assigned registers:
;   r0x1005
;   r0x1006
;   STK00
;; Starting pCode block
S_MAIN__main	code
_main:	;Function start
; 2 exit points
;	.line	21; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	file_clrRam();
	CALL	_file_clrRam
;	.line	22; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	file_init();					//初始化
	CALL	_file_init
;	.line	23; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	file_tc0_Init();
	CALL	_file_tc0_Init
;	.line	24; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	ei();
	ei	
;	.line	25; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	F_FIRST_POWER_UP = 1;
	BTS	_U_Flage1,6
;	.line	26; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	r_g_workMod = 0;
	CLR	_r_g_workMod
;	.line	27; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	F_CHARGE = 0;
	BTC	_U_Flage1,4
;	.line	28; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	F_CHARGE_FULL = 0;
	BTC	_U_Flage1,5
_00125_DS_:
;	.line	32; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	cwdt();				//清看门狗
	cwdt	
;	.line	34; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	if(Time_10ms == 1)
	CLR	r0x1005
	JBTC	_U_Flage1,0
	INC	r0x1005
;;106	MOV	A,r0x1005
;;105	MOV	A,r0x1006
	MOV	A,r0x1005
	MOV	r0x1006,A
	XOR	A,@0x01
	JBTS	STATUS,2
	JMP	_00121_DS_
;	.line	36; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	Time_10ms = 0;	
	BTC	_U_Flage1,0
;	.line	37; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	sleep_scan();
	CALL	_sleep_scan
;	.line	40; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	if(r_g_workMod == 1 && F_CHARGE == 0 && F_CHARGE_FULL == 0)
	MOV	A,_r_g_workMod
	XOR	A,@0x01
	JBTS	STATUS,2
	JMP	_00116_DS_
	JBTC	_U_Flage1,4
	JMP	_00116_DS_
	JBTC	_U_Flage1,5
	JMP	_00116_DS_
;	.line	42; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	SMG_Display(r_g_batVal,0x02);
	MOV	A,@0x02
	MOV	STK00,A
	MOV	A,_r_g_batVal
	CALL	_SMG_Display
;	.line	43; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	Io_Motoer = 1;
	BTS	_PORT6bits,2
	JMP	_00121_DS_
_00116_DS_:
;	.line	47; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	else if(r_g_workMod == 0 && F_CHARGE == 1 && F_CHARGE_FULL == 0)
	MOV	A,@0x00
	OR	A,_r_g_workMod
	JBTS	STATUS,2
	JMP	_00111_DS_
	CLR	r0x1005
	JBTC	_U_Flage1,4
	INC	r0x1005
;;104	MOV	A,r0x1005
;;103	MOV	A,r0x1006
	MOV	A,r0x1005
	MOV	r0x1006,A
	XOR	A,@0x01
	JBTS	STATUS,2
	JMP	_00111_DS_
	JBTC	_U_Flage1,5
	JMP	_00111_DS_
;	.line	49; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	if(++led_turn_cnt >= 50)
	INC	_led_turn_cnt
	MOV	A,@0x32
	SUB	A,_led_turn_cnt
	JBTS	STATUS,0
	JMP	_00106_DS_
;	.line	51; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	led_turn_cnt = 0;
	CLR	_led_turn_cnt
;	.line	52; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	led_turn ^= 0x01;
	MOV	A,@0x01
	XOR	_led_turn,A
_00106_DS_:
;	.line	54; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	SMG_Display(r_g_batVal,led_turn + 0x02);
	MOV	A,@0x02
	ADD	A,_led_turn
	MOV	r0x1005,A
	MOV	A,r0x1005
	MOV	STK00,A
	MOV	A,_r_g_batVal
	CALL	_SMG_Display
;	.line	55; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	Io_Motoer = 0;
	BTC	_PORT6bits,2
	JMP	_00121_DS_
_00111_DS_:
;	.line	58; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	else if(F_CHARGE_FULL == 1)
	CLR	r0x1005
	JBTC	_U_Flage1,5
	INC	r0x1005
;;102	MOV	A,r0x1005
;;101	MOV	A,r0x1006
	MOV	A,r0x1005
	MOV	r0x1006,A
	XOR	A,@0x01
	JBTS	STATUS,2
	JMP	_00108_DS_
;	.line	60; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	SMG_Display(0x64,0x03);
	MOV	A,@0x03
	MOV	STK00,A
	MOV	A,@0x64
	CALL	_SMG_Display
;	.line	61; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	Io_Motoer = 0;
	BTC	_PORT6bits,2
	JMP	_00121_DS_
_00108_DS_:
;	.line	65; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	Io_Motoer = 0;	
	BTC	_PORT6bits,2
_00121_DS_:
;	.line	70; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	if(Time_200us == 1)
	CLR	r0x1005
	JBTC	_U_Flage1,1
	INC	r0x1005
;;100	MOV	A,r0x1005
;;99	MOV	A,r0x1006
	MOV	A,r0x1005
	MOV	r0x1006,A
	XOR	A,@0x01
	JBTS	STATUS,2
	JMP	_00125_DS_
;	.line	72; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	Time_200us = 0;	 
	BTC	_U_Flage1,1
;	.line	73; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	Mode_Check();
	CALL	_Mode_Check
;	.line	74; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	sw_adcBatVal();
	CALL	_sw_adcBatVal
	JMP	_00125_DS_
;	.line	80; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MAIN.C	}
	RET	
; exit point of _main


;	code size estimation:
;	   90+    0 =    90 instructions (  180 byte)

	end
