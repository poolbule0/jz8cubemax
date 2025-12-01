;--------------------------------------------------------
; File Created by SLCC : free open source ANSI-C Compiler
; Version 3.6.0 #Sep 28 2025 (MSVC)
;--------------------------------------------------------
; SL port for the RISC core
;--------------------------------------------------------
;	.file	"C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MODE.C"
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
	global	_Mode_Check
	global	_s_charge_cnt
	global	_s_charge_full_cnt
	global	_s_key_cnt
	global	_key_state
	global	_key_last

;--------------------------------------------------------
; global definitions
;--------------------------------------------------------
UD_MODE_0	udata
_s_charge_cnt	res	1

UD_MODE_1	udata
_s_charge_full_cnt	res	1

UD_MODE_2	udata
_s_key_cnt	res	1

UD_MODE_3	udata
_key_state	res	1

UD_MODE_4	udata
_key_last	res	1

;--------------------------------------------------------
; absolute symbol definitions
;--------------------------------------------------------
;--------------------------------------------------------
; compiler-defined variables
;--------------------------------------------------------
UDL_MODE_0	udata
r0x1007	res	1
;--------------------------------------------------------
; initialized data
;--------------------------------------------------------

;@Allocation info for local variables in function 'Mode_Check'
;@Mode_Check RSRbits                   Allocated to registers ;size:1
;@Mode_Check PCHbits                   Allocated to registers ;size:1
;@Mode_Check PCLbits                   Allocated to registers ;size:1
;@Mode_Check STATUSbits                Allocated to registers ;size:1
;@Mode_Check TC0CONbits                Allocated to registers ;size:1
;@Mode_Check TC0Cbits                  Allocated to registers ;size:1
;@Mode_Check TBRDHbits                 Allocated to registers ;size:1
;@Mode_Check TBRDLbits                 Allocated to registers ;size:1
;@Mode_Check CPUCONbits                Allocated to registers ;size:1
;@Mode_Check IHRCCALbits               Allocated to registers ;size:1
;@Mode_Check PORT5bits                 Allocated to registers ;size:1
;@Mode_Check PORT6bits                 Allocated to registers ;size:1
;@Mode_Check P5CONbits                 Allocated to registers ;size:1
;@Mode_Check P6CONbits                 Allocated to registers ;size:1
;@Mode_Check P5PHbits                  Allocated to registers ;size:1
;@Mode_Check P6PHbits                  Allocated to registers ;size:1
;@Mode_Check P5PDbits                  Allocated to registers ;size:1
;@Mode_Check P6PDbits                  Allocated to registers ;size:1
;@Mode_Check P6ODbits                  Allocated to registers ;size:1
;@Mode_Check P6WDbits                  Allocated to registers ;size:1
;@Mode_Check P5IWEbits                 Allocated to registers ;size:1
;@Mode_Check P6IWEbits                 Allocated to registers ;size:1
;@Mode_Check P5ADEbits                 Allocated to registers ;size:1
;@Mode_Check P6ADEbits                 Allocated to registers ;size:1
;@Mode_Check ADATHbits                 Allocated to registers ;size:1
;@Mode_Check ADATLbits                 Allocated to registers ;size:1
;@Mode_Check ADISbits                  Allocated to registers ;size:1
;@Mode_Check ADCON0bits                Allocated to registers ;size:1
;@Mode_Check ADCON1bits                Allocated to registers ;size:1
;@Mode_Check WDTCONbits                Allocated to registers ;size:1
;@Mode_Check TC1CONbits                Allocated to registers ;size:1
;@Mode_Check TC1PRDLbits               Allocated to registers ;size:1
;@Mode_Check PWM1DTLbits               Allocated to registers ;size:1
;@Mode_Check TC1PRDTHbits              Allocated to registers ;size:1
;@Mode_Check TC1CHbits                 Allocated to registers ;size:1
;@Mode_Check TC1CLbits                 Allocated to registers ;size:1
;@Mode_Check TC2CONbits                Allocated to registers ;size:1
;@Mode_Check TC2PRDLbits               Allocated to registers ;size:1
;@Mode_Check PWM2DTLbits               Allocated to registers ;size:1
;@Mode_Check TC2PRDTHbits              Allocated to registers ;size:1
;@Mode_Check TC2CHbits                 Allocated to registers ;size:1
;@Mode_Check TC2CLbits                 Allocated to registers ;size:1
;@Mode_Check PWM3DTHbits               Allocated to registers ;size:1
;@Mode_Check PWM3DTLbits               Allocated to registers ;size:1
;@Mode_Check PWM4DTHbits               Allocated to registers ;size:1
;@Mode_Check PWM4DTLbits               Allocated to registers ;size:1
;@Mode_Check PWMISbits                 Allocated to registers ;size:1
;@Mode_Check DEADCONbits               Allocated to registers ;size:1
;@Mode_Check PWMCONbits                Allocated to registers ;size:1
;@Mode_Check DEADT0bits                Allocated to registers ;size:1
;@Mode_Check DEADT1bits                Allocated to registers ;size:1
;@Mode_Check INTE0bits                 Allocated to registers ;size:1
;@Mode_Check INTE1bits                 Allocated to registers ;size:1
;@Mode_Check INTF0bits                 Allocated to registers ;size:1
;@Mode_Check INTF1bits                 Allocated to registers ;size:1
;@Mode_Check IARbits                   Allocated to registers ;size:1
;@Mode_Check U_Flage1                  Allocated to registers ;size:1
;@Mode_Check r_g_workMod               Allocated to registers ;size:1
;@Mode_Check s_charge_cnt              Allocated to registers ;size:1
;@Mode_Check s_charge_full_cnt         Allocated to registers ;size:1
;@Mode_Check s_key_cnt                 Allocated to registers ;size:1
;@Mode_Check key_state                 Allocated to registers ;size:1
;@Mode_Check key_last                  Allocated to registers ;size:1
;@Mode_Check RSR                       Allocated to registers ;size:1
;@Mode_Check PCH                       Allocated to registers ;size:1
;@Mode_Check PCL                       Allocated to registers ;size:1
;@Mode_Check STATUS                    Allocated to registers ;size:1
;@Mode_Check TC0CON                    Allocated to registers ;size:1
;@Mode_Check TC0C                      Allocated to registers ;size:1
;@Mode_Check TBRDH                     Allocated to registers ;size:1
;@Mode_Check TBRDL                     Allocated to registers ;size:1
;@Mode_Check CPUCON                    Allocated to registers ;size:1
;@Mode_Check IHRCCAL                   Allocated to registers ;size:1
;@Mode_Check PORT5                     Allocated to registers ;size:1
;@Mode_Check PORT6                     Allocated to registers ;size:1
;@Mode_Check P5CON                     Allocated to registers ;size:1
;@Mode_Check P6CON                     Allocated to registers ;size:1
;@Mode_Check P5PH                      Allocated to registers ;size:1
;@Mode_Check P6PH                      Allocated to registers ;size:1
;@Mode_Check P5PD                      Allocated to registers ;size:1
;@Mode_Check P6PD                      Allocated to registers ;size:1
;@Mode_Check P6OD                      Allocated to registers ;size:1
;@Mode_Check P6WD                      Allocated to registers ;size:1
;@Mode_Check P5IWE                     Allocated to registers ;size:1
;@Mode_Check P6IWE                     Allocated to registers ;size:1
;@Mode_Check P5ADE                     Allocated to registers ;size:1
;@Mode_Check P6ADE                     Allocated to registers ;size:1
;@Mode_Check ADATH                     Allocated to registers ;size:1
;@Mode_Check ADATL                     Allocated to registers ;size:1
;@Mode_Check ADIS                      Allocated to registers ;size:1
;@Mode_Check ADCON0                    Allocated to registers ;size:1
;@Mode_Check ADCON1                    Allocated to registers ;size:1
;@Mode_Check WDTCON                    Allocated to registers ;size:1
;@Mode_Check TC1CON                    Allocated to registers ;size:1
;@Mode_Check TC1PRDL                   Allocated to registers ;size:1
;@Mode_Check PWM1DTL                   Allocated to registers ;size:1
;@Mode_Check TC1PRDTH                  Allocated to registers ;size:1
;@Mode_Check TC1CH                     Allocated to registers ;size:1
;@Mode_Check TC1CL                     Allocated to registers ;size:1
;@Mode_Check TC2CON                    Allocated to registers ;size:1
;@Mode_Check TC2PRDL                   Allocated to registers ;size:1
;@Mode_Check PWM2DTL                   Allocated to registers ;size:1
;@Mode_Check TC2PRDTH                  Allocated to registers ;size:1
;@Mode_Check TC2CH                     Allocated to registers ;size:1
;@Mode_Check TC2CL                     Allocated to registers ;size:1
;@Mode_Check PWM3DTH                   Allocated to registers ;size:1
;@Mode_Check PWM3DTL                   Allocated to registers ;size:1
;@Mode_Check PWM4DTH                   Allocated to registers ;size:1
;@Mode_Check PWM4DTL                   Allocated to registers ;size:1
;@Mode_Check PWMIS                     Allocated to registers ;size:1
;@Mode_Check DEADCON                   Allocated to registers ;size:1
;@Mode_Check PWMCON                    Allocated to registers ;size:1
;@Mode_Check DEADT0                    Allocated to registers ;size:1
;@Mode_Check DEADT1                    Allocated to registers ;size:1
;@Mode_Check INTE0                     Allocated to registers ;size:1
;@Mode_Check INTE1                     Allocated to registers ;size:1
;@Mode_Check INTF0                     Allocated to registers ;size:1
;@Mode_Check INTF1                     Allocated to registers ;size:1
;@Mode_Check IAR                       Allocated to registers ;size:1
;@end Allocation info for local variables in function 'Mode_Check';

;--------------------------------------------------------
; overlayable items in internal ram 
;--------------------------------------------------------
;	udata_ovr
;--------------------------------------------------------
; code
;--------------------------------------------------------
code_MODE	code
;***
;  pBlock Stats: dbName = C
;***
;has an exit
;1 compiler assigned register :
;   r0x1007
;; Starting pCode block
S_MODE__Mode_Check	code
_Mode_Check:	;Function start
; 2 exit points
;	.line	24; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MODE.C	if (Io_Charge == 0 )
	JBTC	_PORT6bits,5
	JMP	_00108_DS_
;	.line	26; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MODE.C	if (++s_charge_cnt >= 15)
	INC	_s_charge_cnt
	MOV	A,@0x0f
	SUB	A,_s_charge_cnt
	JBTS	STATUS,0
	JMP	_00109_DS_
;	.line	29; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MODE.C	F_CHARGE = 1;
	BTS	_U_Flage1,4
;	.line	30; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MODE.C	r_g_workMod = 0;
	CLR	_r_g_workMod
;	.line	32; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MODE.C	s_key_cnt = 0; 
	CLR	_s_key_cnt
	JMP	_00109_DS_
_00108_DS_:
;	.line	37; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MODE.C	s_charge_cnt = 0;
	CLR	_s_charge_cnt
;	.line	38; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MODE.C	F_CHARGE = 0;
	BTC	_U_Flage1,4
_00109_DS_:
;	.line	41; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MODE.C	if(Io_Charge_full == 0)
	JBTC	_PORT6bits,4
	JMP	_00113_DS_
;	.line	43; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MODE.C	if (++s_charge_full_cnt >= 15)
	INC	_s_charge_full_cnt
	MOV	A,@0x0f
	SUB	A,_s_charge_full_cnt
	JBTS	STATUS,0
	JMP	_00114_DS_
;	.line	45; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MODE.C	F_CHARGE_FULL = 1;
	BTS	_U_Flage1,5
;	.line	46; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MODE.C	r_g_workMod = 0;
	CLR	_r_g_workMod
;	.line	47; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MODE.C	F_CHARGE = 1;
	BTS	_U_Flage1,4
;	.line	48; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MODE.C	s_charge_cnt = 0;
	CLR	_s_charge_cnt
;	.line	49; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MODE.C	s_key_cnt = 0;
	CLR	_s_key_cnt
	JMP	_00114_DS_
_00113_DS_:
;	.line	55; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MODE.C	s_charge_full_cnt = 0;
	CLR	_s_charge_full_cnt
;	.line	56; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MODE.C	F_CHARGE_FULL = 0;
	BTC	_U_Flage1,5
_00114_DS_:
;	.line	60; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MODE.C	if (Io_Key == 0)
	JBTC	_PORT6bits,3
	JMP	_00118_DS_
;	.line	62; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MODE.C	if (++s_key_cnt >= 15)
	INC	_s_key_cnt
	MOV	A,@0x0f
	SUB	A,_s_key_cnt
	JBTS	STATUS,0
	JMP	_00119_DS_
;	.line	64; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MODE.C	key_state = 1;
	MOV	A,@0x01
	MOV	_key_state,A
	JMP	_00119_DS_
_00118_DS_:
;	.line	69; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MODE.C	s_key_cnt = 0;
	CLR	_s_key_cnt
;	.line	70; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MODE.C	key_state = 0;
	CLR	_key_state
_00119_DS_:
;	.line	74; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MODE.C	if (key_state == 1 && key_last == 0)
	MOV	A,_key_state
	XOR	A,@0x01
	JBTS	STATUS,2
	JMP	_00121_DS_
	MOV	A,@0x00
	OR	A,_key_last
	JBTS	STATUS,2
	JMP	_00121_DS_
;	.line	77; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MODE.C	F_CHARGE = 0;
	BTC	_U_Flage1,4
;	.line	78; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MODE.C	r_g_workMod = (r_g_workMod == 0) ? 1 : 0;  // ×´Ì¬ÇÐ»»
	MOV	A,@0x00
	OR	A,_r_g_workMod
	JBTS	STATUS,2
	JMP	_00125_DS_
	MOV	A,@0x01
	MOV	r0x1007,A
	JMP	_00126_DS_
_00125_DS_:
	CLR	r0x1007
_00126_DS_:
	MOV	A,r0x1007
	MOV	_r_g_workMod,A
_00121_DS_:
;	.line	82; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MODE.C	key_last = key_state;
	MOV	A,_key_state
	MOV	_key_last,A
;	.line	84; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\MODE.C	}
	RET	
; exit point of _Mode_Check


;	code size estimation:
;	   62+    0 =    62 instructions (  124 byte)

	end
