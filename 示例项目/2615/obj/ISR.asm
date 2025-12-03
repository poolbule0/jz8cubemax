;--------------------------------------------------------
; File Created by SLCC : free open source ANSI-C Compiler
; Version 3.6.0 #Sep 28 2025 (MSVC)
;--------------------------------------------------------
; SL port for the RISC core
;--------------------------------------------------------
;	.file	"C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ISR.C"
	list	p=JZ8P2615
	radix dec
	include "JZ8P2615.inc"
;--------------------------------------------------------
; external declarations
;--------------------------------------------------------
	extern	_SMG_Display
	extern	_SMG_Scan
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
	global	_int_isr
	global	_reg_200us
	global	_reg_10ms
	global	_A_Buff
	global	_S_Buff

;--------------------------------------------------------
; global definitions
;--------------------------------------------------------
UD_ISR_0	udata
_reg_200us	res	1

UD_ISR_1	udata
_reg_10ms	res	1

;--------------------------------------------------------
; absolute symbol definitions
;--------------------------------------------------------
UD_abs_ISR_0	udata_ovr	0x0000
_A_Buff
	res	1
UD_abs_ISR_1	udata_ovr	0x0001
_S_Buff
	res	1
;--------------------------------------------------------
; compiler-defined variables
;--------------------------------------------------------
UDL_ISR_0	udata
r0x1004	res	1
r0x1005	res	1
;--------------------------------------------------------
; initialized data
;--------------------------------------------------------

;@Allocation info for local variables in function 'int_isr'
;@int_isr SMG_Display               Allocated to registers ;size:2
;@int_isr SMG_Scan                  Allocated to registers ;size:2
;@int_isr int_isr                   Allocated to registers ;size:2
;@int_isr RSRbits                   Allocated to registers ;size:1
;@int_isr PCHbits                   Allocated to registers ;size:1
;@int_isr PCLbits                   Allocated to registers ;size:1
;@int_isr STATUSbits                Allocated to registers ;size:1
;@int_isr TC0CONbits                Allocated to registers ;size:1
;@int_isr TC0Cbits                  Allocated to registers ;size:1
;@int_isr TBRDHbits                 Allocated to registers ;size:1
;@int_isr TBRDLbits                 Allocated to registers ;size:1
;@int_isr CPUCONbits                Allocated to registers ;size:1
;@int_isr IHRCCALbits               Allocated to registers ;size:1
;@int_isr PORT5bits                 Allocated to registers ;size:1
;@int_isr PORT6bits                 Allocated to registers ;size:1
;@int_isr P5CONbits                 Allocated to registers ;size:1
;@int_isr P6CONbits                 Allocated to registers ;size:1
;@int_isr P5PHbits                  Allocated to registers ;size:1
;@int_isr P6PHbits                  Allocated to registers ;size:1
;@int_isr P5PDbits                  Allocated to registers ;size:1
;@int_isr P6PDbits                  Allocated to registers ;size:1
;@int_isr P6ODbits                  Allocated to registers ;size:1
;@int_isr P6WDbits                  Allocated to registers ;size:1
;@int_isr P5IWEbits                 Allocated to registers ;size:1
;@int_isr P6IWEbits                 Allocated to registers ;size:1
;@int_isr P5ADEbits                 Allocated to registers ;size:1
;@int_isr P6ADEbits                 Allocated to registers ;size:1
;@int_isr ADATHbits                 Allocated to registers ;size:1
;@int_isr ADATLbits                 Allocated to registers ;size:1
;@int_isr ADISbits                  Allocated to registers ;size:1
;@int_isr ADCON0bits                Allocated to registers ;size:1
;@int_isr ADCON1bits                Allocated to registers ;size:1
;@int_isr WDTCONbits                Allocated to registers ;size:1
;@int_isr TC1CONbits                Allocated to registers ;size:1
;@int_isr TC1PRDLbits               Allocated to registers ;size:1
;@int_isr PWM1DTLbits               Allocated to registers ;size:1
;@int_isr TC1PRDTHbits              Allocated to registers ;size:1
;@int_isr TC1CHbits                 Allocated to registers ;size:1
;@int_isr TC1CLbits                 Allocated to registers ;size:1
;@int_isr TC2CONbits                Allocated to registers ;size:1
;@int_isr TC2PRDLbits               Allocated to registers ;size:1
;@int_isr PWM2DTLbits               Allocated to registers ;size:1
;@int_isr TC2PRDTHbits              Allocated to registers ;size:1
;@int_isr TC2CHbits                 Allocated to registers ;size:1
;@int_isr TC2CLbits                 Allocated to registers ;size:1
;@int_isr PWM3DTHbits               Allocated to registers ;size:1
;@int_isr PWM3DTLbits               Allocated to registers ;size:1
;@int_isr PWM4DTHbits               Allocated to registers ;size:1
;@int_isr PWM4DTLbits               Allocated to registers ;size:1
;@int_isr PWMISbits                 Allocated to registers ;size:1
;@int_isr DEADCONbits               Allocated to registers ;size:1
;@int_isr PWMCONbits                Allocated to registers ;size:1
;@int_isr DEADT0bits                Allocated to registers ;size:1
;@int_isr DEADT1bits                Allocated to registers ;size:1
;@int_isr INTE0bits                 Allocated to registers ;size:1
;@int_isr INTE1bits                 Allocated to registers ;size:1
;@int_isr INTF0bits                 Allocated to registers ;size:1
;@int_isr INTF1bits                 Allocated to registers ;size:1
;@int_isr IARbits                   Allocated to registers ;size:1
;@int_isr U_Flage1                  Allocated to registers ;size:1
;@int_isr r_g_workMod               Allocated to registers ;size:1
;@int_isr Flag_Led1                 Allocated to registers ;size:1
;@int_isr Flag_Led2                 Allocated to registers ;size:1
;@int_isr Flag_Led3                 Allocated to registers ;size:1
;@int_isr Flag_Led4                 Allocated to registers ;size:1
;@int_isr reg_200us                 Allocated to registers ;size:1
;@int_isr reg_10ms                  Allocated to registers ;size:1
;@int_isr A_Buff                    Allocated to registers ;size:1
;@int_isr S_Buff                    Allocated to registers ;size:1
;@int_isr RSR                       Allocated to registers ;size:1
;@int_isr PCH                       Allocated to registers ;size:1
;@int_isr PCL                       Allocated to registers ;size:1
;@int_isr STATUS                    Allocated to registers ;size:1
;@int_isr TC0CON                    Allocated to registers ;size:1
;@int_isr TC0C                      Allocated to registers ;size:1
;@int_isr TBRDH                     Allocated to registers ;size:1
;@int_isr TBRDL                     Allocated to registers ;size:1
;@int_isr CPUCON                    Allocated to registers ;size:1
;@int_isr IHRCCAL                   Allocated to registers ;size:1
;@int_isr PORT5                     Allocated to registers ;size:1
;@int_isr PORT6                     Allocated to registers ;size:1
;@int_isr P5CON                     Allocated to registers ;size:1
;@int_isr P6CON                     Allocated to registers ;size:1
;@int_isr P5PH                      Allocated to registers ;size:1
;@int_isr P6PH                      Allocated to registers ;size:1
;@int_isr P5PD                      Allocated to registers ;size:1
;@int_isr P6PD                      Allocated to registers ;size:1
;@int_isr P6OD                      Allocated to registers ;size:1
;@int_isr P6WD                      Allocated to registers ;size:1
;@int_isr P5IWE                     Allocated to registers ;size:1
;@int_isr P6IWE                     Allocated to registers ;size:1
;@int_isr P5ADE                     Allocated to registers ;size:1
;@int_isr P6ADE                     Allocated to registers ;size:1
;@int_isr ADATH                     Allocated to registers ;size:1
;@int_isr ADATL                     Allocated to registers ;size:1
;@int_isr ADIS                      Allocated to registers ;size:1
;@int_isr ADCON0                    Allocated to registers ;size:1
;@int_isr ADCON1                    Allocated to registers ;size:1
;@int_isr WDTCON                    Allocated to registers ;size:1
;@int_isr TC1CON                    Allocated to registers ;size:1
;@int_isr TC1PRDL                   Allocated to registers ;size:1
;@int_isr PWM1DTL                   Allocated to registers ;size:1
;@int_isr TC1PRDTH                  Allocated to registers ;size:1
;@int_isr TC1CH                     Allocated to registers ;size:1
;@int_isr TC1CL                     Allocated to registers ;size:1
;@int_isr TC2CON                    Allocated to registers ;size:1
;@int_isr TC2PRDL                   Allocated to registers ;size:1
;@int_isr PWM2DTL                   Allocated to registers ;size:1
;@int_isr TC2PRDTH                  Allocated to registers ;size:1
;@int_isr TC2CH                     Allocated to registers ;size:1
;@int_isr TC2CL                     Allocated to registers ;size:1
;@int_isr PWM3DTH                   Allocated to registers ;size:1
;@int_isr PWM3DTL                   Allocated to registers ;size:1
;@int_isr PWM4DTH                   Allocated to registers ;size:1
;@int_isr PWM4DTL                   Allocated to registers ;size:1
;@int_isr PWMIS                     Allocated to registers ;size:1
;@int_isr DEADCON                   Allocated to registers ;size:1
;@int_isr PWMCON                    Allocated to registers ;size:1
;@int_isr DEADT0                    Allocated to registers ;size:1
;@int_isr DEADT1                    Allocated to registers ;size:1
;@int_isr INTE0                     Allocated to registers ;size:1
;@int_isr INTE1                     Allocated to registers ;size:1
;@int_isr INTF0                     Allocated to registers ;size:1
;@int_isr INTF1                     Allocated to registers ;size:1
;@int_isr IAR                       Allocated to registers ;size:1
;@end Allocation info for local variables in function 'int_isr';

;--------------------------------------------------------
; overlayable items in internal ram 
;--------------------------------------------------------
;	udata_ovr
;--------------------------------------------------------
; interrupt and initialization code
;--------------------------------------------------------
c_interrupt	code	0x0003
__sdcc_interrupt:
;***
;  pBlock Stats: dbName = I
;***
;functions called:
;   _SMG_Scan
;   _SMG_Scan
;2 compiler assigned registers:
;   r0x1004
;   r0x1005
;; Starting pCode block
_int_isr:	;Function start
; 0 exit points
;	.line	11; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ISR.C	__asm__("org 0x08");			//中断入口地址	
	org	0x08
;	.line	12; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ISR.C	di();		
	di	
;	.line	13; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ISR.C	push(A_Buff, S_Buff);			//中断入栈保护
	mov	_A_Buff,a
	swap	_A_Buff
	swapa	STATUS
	mov	_S_Buff,a
;	.line	15; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ISR.C	if(TC0IF == 1)					//判断TCIF是否为1
	CLR	r0x1004
	JBTC	_INTF0bits,0
	INC	r0x1004
;;102	MOV	A,r0x1004
;;101	MOV	A,r0x1005
	MOV	A,r0x1004
	MOV	r0x1005,A
	XOR	A,@0x01
	JBTS	STATUS,2
	JMP	_00113_DS_
;	.line	18; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ISR.C	TC0C  += TCC_NUM;		
	MOV	A,@0xce
	ADD	_TC0C,A
;	.line	19; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ISR.C	TC0IF = 0;		
	BTC	_INTF0bits,0
;	.line	21; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ISR.C	if(++reg_10ms >= 200)
	INC	_reg_10ms
	MOV	A,@0xc8
	SUB	A,_reg_10ms
	JBTS	STATUS,0
	JMP	_00106_DS_
;	.line	23; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ISR.C	reg_10ms  = 0;
	CLR	_reg_10ms
;	.line	24; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ISR.C	Time_10ms = 1;
	BTS	_U_Flage1,0
_00106_DS_:
;	.line	27; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ISR.C	if(++reg_200us >= 4)
	INC	_reg_200us
	MOV	A,@0x04
	SUB	A,_reg_200us
	JBTS	STATUS,0
	JMP	_00108_DS_
;	.line	29; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ISR.C	reg_200us  = 0;
	CLR	_reg_200us
;	.line	30; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ISR.C	Time_200us = 1;
	BTS	_U_Flage1,1
_00108_DS_:
;	.line	32; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ISR.C	if(r_g_workMod == 1 || F_CHARGE == 1)
	MOV	A,_r_g_workMod
	XOR	A,@0x01
	JBTS	STATUS,2
	JMP	_00130_DS_
	JMP	_00109_DS_
_00130_DS_:
	CLR	r0x1004
	JBTC	_U_Flage1,4
	INC	r0x1004
;;100	MOV	A,r0x1004
;;99	MOV	A,r0x1005
	MOV	A,r0x1004
	MOV	r0x1005,A
	XOR	A,@0x01
	JBTS	STATUS,2
	JMP	_00113_DS_
_00109_DS_:
;	.line	34; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ISR.C	SMG_Scan();
	CALL	_SMG_Scan
_00113_DS_:
;	.line	39; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ISR.C	INTF0=0x01;						//清除不用的标志位
	MOV	A,@0x01
	MOV	_INTF0,A
;	.line	40; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ISR.C	INTF1=0x00;
	CLR	_INTF1
;	.line	41; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ISR.C	pop(A_Buff, S_Buff);			//中断出栈保护恢复
	swapa	_S_Buff
	mov	STATUS,a
	swapa	_A_Buff
;	.line	42; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ISR.C	ei();
	ei	
;	.line	43; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ISR.C	ret();
	ret	
;	.line	45; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ISR.C	}
END_OF_INTERRUPT:
	RETI	

;--------------------------------------------------------
; code
;--------------------------------------------------------
code_ISR	code

;	code size estimation:
;	   43+    0 =    43 instructions (   86 byte)

	end
