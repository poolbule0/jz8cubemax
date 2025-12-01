;--------------------------------------------------------
; File Created by SLCC : free open source ANSI-C Compiler
; Version 3.6.0 #Sep 28 2025 (MSVC)
;--------------------------------------------------------
; SL port for the RISC core
;--------------------------------------------------------
;	.file	"C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C"
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
	global	_sleep_scan
	global	_sleep_cnt

;--------------------------------------------------------
; global definitions
;--------------------------------------------------------
;--------------------------------------------------------
; absolute symbol definitions
;--------------------------------------------------------
;--------------------------------------------------------
; compiler-defined variables
;--------------------------------------------------------
;--------------------------------------------------------
; initialized data
;--------------------------------------------------------

ID_SLEEP_0	idata
_sleep_cnt
	add 0x182,a
	db	0x00


;@Allocation info for local variables in function 'sleep_scan'
;@sleep_scan RSRbits                   Allocated to registers ;size:1
;@sleep_scan PCHbits                   Allocated to registers ;size:1
;@sleep_scan PCLbits                   Allocated to registers ;size:1
;@sleep_scan STATUSbits                Allocated to registers ;size:1
;@sleep_scan TC0CONbits                Allocated to registers ;size:1
;@sleep_scan TC0Cbits                  Allocated to registers ;size:1
;@sleep_scan TBRDHbits                 Allocated to registers ;size:1
;@sleep_scan TBRDLbits                 Allocated to registers ;size:1
;@sleep_scan CPUCONbits                Allocated to registers ;size:1
;@sleep_scan IHRCCALbits               Allocated to registers ;size:1
;@sleep_scan PORT5bits                 Allocated to registers ;size:1
;@sleep_scan PORT6bits                 Allocated to registers ;size:1
;@sleep_scan P5CONbits                 Allocated to registers ;size:1
;@sleep_scan P6CONbits                 Allocated to registers ;size:1
;@sleep_scan P5PHbits                  Allocated to registers ;size:1
;@sleep_scan P6PHbits                  Allocated to registers ;size:1
;@sleep_scan P5PDbits                  Allocated to registers ;size:1
;@sleep_scan P6PDbits                  Allocated to registers ;size:1
;@sleep_scan P6ODbits                  Allocated to registers ;size:1
;@sleep_scan P6WDbits                  Allocated to registers ;size:1
;@sleep_scan P5IWEbits                 Allocated to registers ;size:1
;@sleep_scan P6IWEbits                 Allocated to registers ;size:1
;@sleep_scan P5ADEbits                 Allocated to registers ;size:1
;@sleep_scan P6ADEbits                 Allocated to registers ;size:1
;@sleep_scan ADATHbits                 Allocated to registers ;size:1
;@sleep_scan ADATLbits                 Allocated to registers ;size:1
;@sleep_scan ADISbits                  Allocated to registers ;size:1
;@sleep_scan ADCON0bits                Allocated to registers ;size:1
;@sleep_scan ADCON1bits                Allocated to registers ;size:1
;@sleep_scan WDTCONbits                Allocated to registers ;size:1
;@sleep_scan TC1CONbits                Allocated to registers ;size:1
;@sleep_scan TC1PRDLbits               Allocated to registers ;size:1
;@sleep_scan PWM1DTLbits               Allocated to registers ;size:1
;@sleep_scan TC1PRDTHbits              Allocated to registers ;size:1
;@sleep_scan TC1CHbits                 Allocated to registers ;size:1
;@sleep_scan TC1CLbits                 Allocated to registers ;size:1
;@sleep_scan TC2CONbits                Allocated to registers ;size:1
;@sleep_scan TC2PRDLbits               Allocated to registers ;size:1
;@sleep_scan PWM2DTLbits               Allocated to registers ;size:1
;@sleep_scan TC2PRDTHbits              Allocated to registers ;size:1
;@sleep_scan TC2CHbits                 Allocated to registers ;size:1
;@sleep_scan TC2CLbits                 Allocated to registers ;size:1
;@sleep_scan PWM3DTHbits               Allocated to registers ;size:1
;@sleep_scan PWM3DTLbits               Allocated to registers ;size:1
;@sleep_scan PWM4DTHbits               Allocated to registers ;size:1
;@sleep_scan PWM4DTLbits               Allocated to registers ;size:1
;@sleep_scan PWMISbits                 Allocated to registers ;size:1
;@sleep_scan DEADCONbits               Allocated to registers ;size:1
;@sleep_scan PWMCONbits                Allocated to registers ;size:1
;@sleep_scan DEADT0bits                Allocated to registers ;size:1
;@sleep_scan DEADT1bits                Allocated to registers ;size:1
;@sleep_scan INTE0bits                 Allocated to registers ;size:1
;@sleep_scan INTE1bits                 Allocated to registers ;size:1
;@sleep_scan INTF0bits                 Allocated to registers ;size:1
;@sleep_scan INTF1bits                 Allocated to registers ;size:1
;@sleep_scan IARbits                   Allocated to registers ;size:1
;@sleep_scan U_Flage1                  Allocated to registers ;size:1
;@sleep_scan r_g_workMod               Allocated to registers ;size:1
;@sleep_scan sleep_cnt                 Allocated to registers ;size:1
;@sleep_scan RSR                       Allocated to registers ;size:1
;@sleep_scan PCH                       Allocated to registers ;size:1
;@sleep_scan PCL                       Allocated to registers ;size:1
;@sleep_scan STATUS                    Allocated to registers ;size:1
;@sleep_scan TC0CON                    Allocated to registers ;size:1
;@sleep_scan TC0C                      Allocated to registers ;size:1
;@sleep_scan TBRDH                     Allocated to registers ;size:1
;@sleep_scan TBRDL                     Allocated to registers ;size:1
;@sleep_scan CPUCON                    Allocated to registers ;size:1
;@sleep_scan IHRCCAL                   Allocated to registers ;size:1
;@sleep_scan PORT5                     Allocated to registers ;size:1
;@sleep_scan PORT6                     Allocated to registers ;size:1
;@sleep_scan P5CON                     Allocated to registers ;size:1
;@sleep_scan P6CON                     Allocated to registers ;size:1
;@sleep_scan P5PH                      Allocated to registers ;size:1
;@sleep_scan P6PH                      Allocated to registers ;size:1
;@sleep_scan P5PD                      Allocated to registers ;size:1
;@sleep_scan P6PD                      Allocated to registers ;size:1
;@sleep_scan P6OD                      Allocated to registers ;size:1
;@sleep_scan P6WD                      Allocated to registers ;size:1
;@sleep_scan P5IWE                     Allocated to registers ;size:1
;@sleep_scan P6IWE                     Allocated to registers ;size:1
;@sleep_scan P5ADE                     Allocated to registers ;size:1
;@sleep_scan P6ADE                     Allocated to registers ;size:1
;@sleep_scan ADATH                     Allocated to registers ;size:1
;@sleep_scan ADATL                     Allocated to registers ;size:1
;@sleep_scan ADIS                      Allocated to registers ;size:1
;@sleep_scan ADCON0                    Allocated to registers ;size:1
;@sleep_scan ADCON1                    Allocated to registers ;size:1
;@sleep_scan WDTCON                    Allocated to registers ;size:1
;@sleep_scan TC1CON                    Allocated to registers ;size:1
;@sleep_scan TC1PRDL                   Allocated to registers ;size:1
;@sleep_scan PWM1DTL                   Allocated to registers ;size:1
;@sleep_scan TC1PRDTH                  Allocated to registers ;size:1
;@sleep_scan TC1CH                     Allocated to registers ;size:1
;@sleep_scan TC1CL                     Allocated to registers ;size:1
;@sleep_scan TC2CON                    Allocated to registers ;size:1
;@sleep_scan TC2PRDL                   Allocated to registers ;size:1
;@sleep_scan PWM2DTL                   Allocated to registers ;size:1
;@sleep_scan TC2PRDTH                  Allocated to registers ;size:1
;@sleep_scan TC2CH                     Allocated to registers ;size:1
;@sleep_scan TC2CL                     Allocated to registers ;size:1
;@sleep_scan PWM3DTH                   Allocated to registers ;size:1
;@sleep_scan PWM3DTL                   Allocated to registers ;size:1
;@sleep_scan PWM4DTH                   Allocated to registers ;size:1
;@sleep_scan PWM4DTL                   Allocated to registers ;size:1
;@sleep_scan PWMIS                     Allocated to registers ;size:1
;@sleep_scan DEADCON                   Allocated to registers ;size:1
;@sleep_scan PWMCON                    Allocated to registers ;size:1
;@sleep_scan DEADT0                    Allocated to registers ;size:1
;@sleep_scan DEADT1                    Allocated to registers ;size:1
;@sleep_scan INTE0                     Allocated to registers ;size:1
;@sleep_scan INTE1                     Allocated to registers ;size:1
;@sleep_scan INTF0                     Allocated to registers ;size:1
;@sleep_scan INTF1                     Allocated to registers ;size:1
;@sleep_scan IAR                       Allocated to registers ;size:1
;@end Allocation info for local variables in function 'sleep_scan';

;--------------------------------------------------------
; overlayable items in internal ram 
;--------------------------------------------------------
;	udata_ovr
;--------------------------------------------------------
; code
;--------------------------------------------------------
code_SLEEP	code
;***
;  pBlock Stats: dbName = C
;***
;has an exit
;; Starting pCode block
S_SLEEP__sleep_scan	code
_sleep_scan:	;Function start
; 2 exit points
;	.line	10; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	if(F_CHARGE == 0 && F_CHARGE_FULL == 0 && r_g_workMod == 0)
	JBTC	_U_Flage1,4
	JMP	_00108_DS_
	JBTC	_U_Flage1,5
	JMP	_00108_DS_
	MOV	A,@0x00
	OR	A,_r_g_workMod
	JBTS	STATUS,2
	JMP	_00108_DS_
;	.line	12; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	if(++ sleep_cnt >= 5){
	INC	_sleep_cnt
	MOV	A,@0x05
	SUB	A,_sleep_cnt
	JBTS	STATUS,0
	JMP	_00112_DS_
;	.line	13; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	sleep_cnt = 0;
	CLR	_sleep_cnt
;	.line	15; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	ADIS = 0;
	CLR	_ADIS
;	.line	16; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	ADCON0 = 0;	
	CLR	_ADCON0
;	.line	17; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	ADCON1 = 0;
	CLR	_ADCON1
;	.line	18; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	PORT5 = 0x00;
	CLR	_PORT5
;	.line	19; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	PORT6 = 0x00;
	CLR	_PORT6
;	.line	21; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	TC0C = 0;
	CLR	_TC0C
;	.line	22; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	WDTCON = 0x00;	
	CLR	_WDTCON
;	.line	23; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	INTE0=0x04;	
	MOV	A,@0x04
	MOV	_INTE0,A
;	.line	25; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	INTF0 = 0;
	CLR	_INTF0
;	.line	26; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	INTF1 = 0;
	CLR	_INTF1
;	.line	27; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	di();				//禁止唤醒进入中断
	di	
;	.line	28; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	sleep();
	sleep	
;	.line	29; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	nop(); 
	nop	
;	.line	30; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	nop();
	nop	
;	.line	31; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	nop();
	nop	
;	.line	32; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	nop();
	nop	
;	.line	33; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	cwdt();
	cwdt	
;	.line	35; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	INTE0 = 0;	//
	CLR	_INTE0
;	.line	37; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	TC0CON = 0x82;		//TC0控制寄存器			
	MOV	A,@0x82
	MOV	_TC0CON,A
;	.line	38; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	TC0C = TCC_NUM;		//TC0计数寄存器
	MOV	A,@0xce
	MOV	_TC0C,A
;	.line	39; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	INTE0 |= 0x01;		//中断使能 
	BTS	_INTE0,0
;	.line	41; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	INTF0 = 0;
	CLR	_INTF0
;	.line	42; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	INTF1 = 0;
	CLR	_INTF1
;	.line	43; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	ei();	
	ei	
	JMP	_00112_DS_
_00108_DS_:
;	.line	50; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	sleep_cnt = 0;
	CLR	_sleep_cnt
;	.line	53; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\SLEEP.C	}
_00112_DS_:
	RET	
; exit point of _sleep_scan


;	code size estimation:
;	   36+    0 =    36 instructions (   72 byte)

	end
