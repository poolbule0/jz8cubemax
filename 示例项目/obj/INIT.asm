;--------------------------------------------------------
; File Created by SLCC : free open source ANSI-C Compiler
; Version 3.6.0 #Sep 28 2025 (MSVC)
;--------------------------------------------------------
; SL port for the RISC core
;--------------------------------------------------------
;	.file	"C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C"
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
	global	_file_tc0_Init
	global	_file_init
	global	_file_clrRam

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

;@Allocation info for local variables in function 'file_clrRam'
;@file_clrRam file_init                 Allocated to registers ;size:2
;@file_clrRam file_tc0_Init             Allocated to registers ;size:2
;@file_clrRam RSRbits                   Allocated to registers ;size:1
;@file_clrRam PCHbits                   Allocated to registers ;size:1
;@file_clrRam PCLbits                   Allocated to registers ;size:1
;@file_clrRam STATUSbits                Allocated to registers ;size:1
;@file_clrRam TC0CONbits                Allocated to registers ;size:1
;@file_clrRam TC0Cbits                  Allocated to registers ;size:1
;@file_clrRam TBRDHbits                 Allocated to registers ;size:1
;@file_clrRam TBRDLbits                 Allocated to registers ;size:1
;@file_clrRam CPUCONbits                Allocated to registers ;size:1
;@file_clrRam IHRCCALbits               Allocated to registers ;size:1
;@file_clrRam PORT5bits                 Allocated to registers ;size:1
;@file_clrRam PORT6bits                 Allocated to registers ;size:1
;@file_clrRam P5CONbits                 Allocated to registers ;size:1
;@file_clrRam P6CONbits                 Allocated to registers ;size:1
;@file_clrRam P5PHbits                  Allocated to registers ;size:1
;@file_clrRam P6PHbits                  Allocated to registers ;size:1
;@file_clrRam P5PDbits                  Allocated to registers ;size:1
;@file_clrRam P6PDbits                  Allocated to registers ;size:1
;@file_clrRam P6ODbits                  Allocated to registers ;size:1
;@file_clrRam P6WDbits                  Allocated to registers ;size:1
;@file_clrRam P5IWEbits                 Allocated to registers ;size:1
;@file_clrRam P6IWEbits                 Allocated to registers ;size:1
;@file_clrRam P5ADEbits                 Allocated to registers ;size:1
;@file_clrRam P6ADEbits                 Allocated to registers ;size:1
;@file_clrRam ADATHbits                 Allocated to registers ;size:1
;@file_clrRam ADATLbits                 Allocated to registers ;size:1
;@file_clrRam ADISbits                  Allocated to registers ;size:1
;@file_clrRam ADCON0bits                Allocated to registers ;size:1
;@file_clrRam ADCON1bits                Allocated to registers ;size:1
;@file_clrRam WDTCONbits                Allocated to registers ;size:1
;@file_clrRam TC1CONbits                Allocated to registers ;size:1
;@file_clrRam TC1PRDLbits               Allocated to registers ;size:1
;@file_clrRam PWM1DTLbits               Allocated to registers ;size:1
;@file_clrRam TC1PRDTHbits              Allocated to registers ;size:1
;@file_clrRam TC1CHbits                 Allocated to registers ;size:1
;@file_clrRam TC1CLbits                 Allocated to registers ;size:1
;@file_clrRam TC2CONbits                Allocated to registers ;size:1
;@file_clrRam TC2PRDLbits               Allocated to registers ;size:1
;@file_clrRam PWM2DTLbits               Allocated to registers ;size:1
;@file_clrRam TC2PRDTHbits              Allocated to registers ;size:1
;@file_clrRam TC2CHbits                 Allocated to registers ;size:1
;@file_clrRam TC2CLbits                 Allocated to registers ;size:1
;@file_clrRam PWM3DTHbits               Allocated to registers ;size:1
;@file_clrRam PWM3DTLbits               Allocated to registers ;size:1
;@file_clrRam PWM4DTHbits               Allocated to registers ;size:1
;@file_clrRam PWM4DTLbits               Allocated to registers ;size:1
;@file_clrRam PWMISbits                 Allocated to registers ;size:1
;@file_clrRam DEADCONbits               Allocated to registers ;size:1
;@file_clrRam PWMCONbits                Allocated to registers ;size:1
;@file_clrRam DEADT0bits                Allocated to registers ;size:1
;@file_clrRam DEADT1bits                Allocated to registers ;size:1
;@file_clrRam INTE0bits                 Allocated to registers ;size:1
;@file_clrRam INTE1bits                 Allocated to registers ;size:1
;@file_clrRam INTF0bits                 Allocated to registers ;size:1
;@file_clrRam INTF1bits                 Allocated to registers ;size:1
;@file_clrRam IARbits                   Allocated to registers ;size:1
;@file_clrRam U_Flage1                  Allocated to registers ;size:1
;@file_clrRam r_g_workMod               Allocated to registers ;size:1
;@file_clrRam RSR                       Allocated to registers ;size:1
;@file_clrRam PCH                       Allocated to registers ;size:1
;@file_clrRam PCL                       Allocated to registers ;size:1
;@file_clrRam STATUS                    Allocated to registers ;size:1
;@file_clrRam TC0CON                    Allocated to registers ;size:1
;@file_clrRam TC0C                      Allocated to registers ;size:1
;@file_clrRam TBRDH                     Allocated to registers ;size:1
;@file_clrRam TBRDL                     Allocated to registers ;size:1
;@file_clrRam CPUCON                    Allocated to registers ;size:1
;@file_clrRam IHRCCAL                   Allocated to registers ;size:1
;@file_clrRam PORT5                     Allocated to registers ;size:1
;@file_clrRam PORT6                     Allocated to registers ;size:1
;@file_clrRam P5CON                     Allocated to registers ;size:1
;@file_clrRam P6CON                     Allocated to registers ;size:1
;@file_clrRam P5PH                      Allocated to registers ;size:1
;@file_clrRam P6PH                      Allocated to registers ;size:1
;@file_clrRam P5PD                      Allocated to registers ;size:1
;@file_clrRam P6PD                      Allocated to registers ;size:1
;@file_clrRam P6OD                      Allocated to registers ;size:1
;@file_clrRam P6WD                      Allocated to registers ;size:1
;@file_clrRam P5IWE                     Allocated to registers ;size:1
;@file_clrRam P6IWE                     Allocated to registers ;size:1
;@file_clrRam P5ADE                     Allocated to registers ;size:1
;@file_clrRam P6ADE                     Allocated to registers ;size:1
;@file_clrRam ADATH                     Allocated to registers ;size:1
;@file_clrRam ADATL                     Allocated to registers ;size:1
;@file_clrRam ADIS                      Allocated to registers ;size:1
;@file_clrRam ADCON0                    Allocated to registers ;size:1
;@file_clrRam ADCON1                    Allocated to registers ;size:1
;@file_clrRam WDTCON                    Allocated to registers ;size:1
;@file_clrRam TC1CON                    Allocated to registers ;size:1
;@file_clrRam TC1PRDL                   Allocated to registers ;size:1
;@file_clrRam PWM1DTL                   Allocated to registers ;size:1
;@file_clrRam TC1PRDTH                  Allocated to registers ;size:1
;@file_clrRam TC1CH                     Allocated to registers ;size:1
;@file_clrRam TC1CL                     Allocated to registers ;size:1
;@file_clrRam TC2CON                    Allocated to registers ;size:1
;@file_clrRam TC2PRDL                   Allocated to registers ;size:1
;@file_clrRam PWM2DTL                   Allocated to registers ;size:1
;@file_clrRam TC2PRDTH                  Allocated to registers ;size:1
;@file_clrRam TC2CH                     Allocated to registers ;size:1
;@file_clrRam TC2CL                     Allocated to registers ;size:1
;@file_clrRam PWM3DTH                   Allocated to registers ;size:1
;@file_clrRam PWM3DTL                   Allocated to registers ;size:1
;@file_clrRam PWM4DTH                   Allocated to registers ;size:1
;@file_clrRam PWM4DTL                   Allocated to registers ;size:1
;@file_clrRam PWMIS                     Allocated to registers ;size:1
;@file_clrRam DEADCON                   Allocated to registers ;size:1
;@file_clrRam PWMCON                    Allocated to registers ;size:1
;@file_clrRam DEADT0                    Allocated to registers ;size:1
;@file_clrRam DEADT1                    Allocated to registers ;size:1
;@file_clrRam INTE0                     Allocated to registers ;size:1
;@file_clrRam INTE1                     Allocated to registers ;size:1
;@file_clrRam INTF0                     Allocated to registers ;size:1
;@file_clrRam INTF1                     Allocated to registers ;size:1
;@file_clrRam IAR                       Allocated to registers ;size:1
;@end Allocation info for local variables in function 'file_clrRam';

;--------------------------------------------------------
; overlayable items in internal ram 
;--------------------------------------------------------
;	udata_ovr
;--------------------------------------------------------
; code
;--------------------------------------------------------
code_INIT	code
;***
;  pBlock Stats: dbName = C
;***
;has an exit
;; Starting pCode block
S_INIT__file_tc0_Init	code
_file_tc0_Init:	;Function start
; 2 exit points
;	.line	48; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C	TC0CON = 0x82;	//TC0控制寄存器			0分频	
	MOV	A,@0x82
	MOV	_TC0CON,A
;	.line	49; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C	TC0C = TCC_NUM;		//TC0计数寄存器
	MOV	A,@0xce
	MOV	_TC0C,A
;	.line	50; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C	INTE0 |= 0x01;			//中断使能 21
	BTS	_INTE0,0
;	.line	51; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C	}
	RET	
; exit point of _file_tc0_Init

;***
;  pBlock Stats: dbName = C
;***
;has an exit
;; Starting pCode block
S_INIT__file_init	code
_file_init:	;Function start
; 2 exit points
;	.line	18; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C	PORT5=0x00;
	CLR	_PORT5
;	.line	19; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C	PORT6=0x00;
	CLR	_PORT6
;	.line	21; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C	P5CON=0x00;			//P5端口控制	;0输出，1输入
	CLR	_P5CON
;	.line	22; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C	P6CON=0x38;			//P6端口控制    ;0输出，1输入
	MOV	A,@0x38
	MOV	_P6CON,A
;	.line	24; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C	P5PH=0xFF;			//P5口上拉		;0使能，1禁止
	MOV	A,@0xff
	MOV	_P5PH,A
;	.line	25; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C	P6PH=0xC7;			//P6口上拉		;0使能，1禁止
	MOV	A,@0xc7
	MOV	_P6PH,A
;	.line	27; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C	P5PD=0xff;			//P5口下拉		;0使能，1禁止
	MOV	A,@0xff
	MOV	_P5PD,A
;	.line	28; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C	P6PD=0xff;			//P6口下拉		;0使能，1禁止	
	MOV	A,@0xff
	MOV	_P6PD,A
;	.line	30; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C	P6OD=0x00;			//P6口开漏		;0禁止，1使能
	CLR	_P6OD
;	.line	31; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C	P6WD=0x00;			//P6口弱驱动   ;0禁止，1使能	
	CLR	_P6WD
;	.line	34; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C	P5IWE=0X00;			//P5口状态变化唤醒使能
	CLR	_P5IWE
;	.line	35; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C	P6IWE=0X38;			//P6口状态变化唤醒使能
	MOV	A,@0x38
	MOV	_P6IWE,A
;	.line	38; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C	WDTCON=0x00;		//bit6&5:P60&P53外部中断功能控制位，0:普通IO口, 1:外部中断口
	CLR	_WDTCON
;	.line	40; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C	INTE0=0x01;			//中断使能 21
	MOV	A,@0x01
	MOV	_INTE0,A
;	.line	41; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C	INTE1=0x00;			//周期及占空比中断
	CLR	_INTE1
;	.line	42; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C	INTF0=0x00;			//清中断标志位
	CLR	_INTF0
;	.line	43; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C	INTF1=0x00;		
	CLR	_INTF1
;	.line	44; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C	}
	RET	
; exit point of _file_init

;***
;  pBlock Stats: dbName = C
;***
;has an exit
;; Starting pCode block
S_INIT__file_clrRam	code
_file_clrRam:	;Function start
; 2 exit points
;	.line	8; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C	for(RSR=0x90;RSR<0xFF;RSR++)	//清零 BANK0 RAM  IAR-R0,RSR-R4
	MOV	A,@0x90
	MOV	_RSR,A
_00107_DS_:
	MOV	A,@0xff
	SUB	A,_RSR
	JBTC	STATUS,0
	JMP	_00105_DS_
;	.line	9; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C	{IAR = 0;}
	CLR	_IAR
;	.line	8; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C	for(RSR=0x90;RSR<0xFF;RSR++)	//清零 BANK0 RAM  IAR-R0,RSR-R4
	INC	_RSR
	JMP	_00107_DS_
_00105_DS_:
;	.line	10; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C	IAR = 0;
	CLR	_IAR
;	.line	11; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\INIT.C	}
	RET	
; exit point of _file_clrRam


;	code size estimation:
;	   42+    0 =    42 instructions (   84 byte)

	end
