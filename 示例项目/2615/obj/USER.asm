;--------------------------------------------------------
; File Created by SLCC : free open source ANSI-C Compiler
; Version 3.6.0 #Sep 28 2025 (MSVC)
;--------------------------------------------------------
; SL port for the RISC core
;--------------------------------------------------------
;	.file	"C:\USERS\ADMINISTRATOR\DESKTOP\培训期项目\抄板2\01_J2615_C\USER.C"
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
	extern	_Flag_Led1
	extern	_Flag_Led2
	extern	_Flag_Led3
	extern	_Flag_Led4
	extern	_U_Flage1
	extern	_r_g_workMod
	extern	_reg_2ms
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
	global	_systemInit
	global	_ramInitial

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

;@Allocation info for local variables in function 'ramInitial'
;@ramInitial SMG_Display               Allocated to registers ;size:2
;@ramInitial SMG_Scan                  Allocated to registers ;size:2
;@ramInitial systemInit                Allocated to registers ;size:2
;@ramInitial RSRbits                   Allocated to registers ;size:1
;@ramInitial PCHbits                   Allocated to registers ;size:1
;@ramInitial PCLbits                   Allocated to registers ;size:1
;@ramInitial STATUSbits                Allocated to registers ;size:1
;@ramInitial TC0CONbits                Allocated to registers ;size:1
;@ramInitial TC0Cbits                  Allocated to registers ;size:1
;@ramInitial TBRDHbits                 Allocated to registers ;size:1
;@ramInitial TBRDLbits                 Allocated to registers ;size:1
;@ramInitial CPUCONbits                Allocated to registers ;size:1
;@ramInitial IHRCCALbits               Allocated to registers ;size:1
;@ramInitial PORT5bits                 Allocated to registers ;size:1
;@ramInitial PORT6bits                 Allocated to registers ;size:1
;@ramInitial P5CONbits                 Allocated to registers ;size:1
;@ramInitial P6CONbits                 Allocated to registers ;size:1
;@ramInitial P5PHbits                  Allocated to registers ;size:1
;@ramInitial P6PHbits                  Allocated to registers ;size:1
;@ramInitial P5PDbits                  Allocated to registers ;size:1
;@ramInitial P6PDbits                  Allocated to registers ;size:1
;@ramInitial P6ODbits                  Allocated to registers ;size:1
;@ramInitial P6WDbits                  Allocated to registers ;size:1
;@ramInitial P5IWEbits                 Allocated to registers ;size:1
;@ramInitial P6IWEbits                 Allocated to registers ;size:1
;@ramInitial P5ADEbits                 Allocated to registers ;size:1
;@ramInitial P6ADEbits                 Allocated to registers ;size:1
;@ramInitial ADATHbits                 Allocated to registers ;size:1
;@ramInitial ADATLbits                 Allocated to registers ;size:1
;@ramInitial ADISbits                  Allocated to registers ;size:1
;@ramInitial ADCON0bits                Allocated to registers ;size:1
;@ramInitial ADCON1bits                Allocated to registers ;size:1
;@ramInitial WDTCONbits                Allocated to registers ;size:1
;@ramInitial TC1CONbits                Allocated to registers ;size:1
;@ramInitial TC1PRDLbits               Allocated to registers ;size:1
;@ramInitial PWM1DTLbits               Allocated to registers ;size:1
;@ramInitial TC1PRDTHbits              Allocated to registers ;size:1
;@ramInitial TC1CHbits                 Allocated to registers ;size:1
;@ramInitial TC1CLbits                 Allocated to registers ;size:1
;@ramInitial TC2CONbits                Allocated to registers ;size:1
;@ramInitial TC2PRDLbits               Allocated to registers ;size:1
;@ramInitial PWM2DTLbits               Allocated to registers ;size:1
;@ramInitial TC2PRDTHbits              Allocated to registers ;size:1
;@ramInitial TC2CHbits                 Allocated to registers ;size:1
;@ramInitial TC2CLbits                 Allocated to registers ;size:1
;@ramInitial PWM3DTHbits               Allocated to registers ;size:1
;@ramInitial PWM3DTLbits               Allocated to registers ;size:1
;@ramInitial PWM4DTHbits               Allocated to registers ;size:1
;@ramInitial PWM4DTLbits               Allocated to registers ;size:1
;@ramInitial PWMISbits                 Allocated to registers ;size:1
;@ramInitial DEADCONbits               Allocated to registers ;size:1
;@ramInitial PWMCONbits                Allocated to registers ;size:1
;@ramInitial DEADT0bits                Allocated to registers ;size:1
;@ramInitial DEADT1bits                Allocated to registers ;size:1
;@ramInitial INTE0bits                 Allocated to registers ;size:1
;@ramInitial INTE1bits                 Allocated to registers ;size:1
;@ramInitial INTF0bits                 Allocated to registers ;size:1
;@ramInitial INTF1bits                 Allocated to registers ;size:1
;@ramInitial IARbits                   Allocated to registers ;size:1
;@ramInitial Flag_Led1                 Allocated to registers ;size:1
;@ramInitial Flag_Led2                 Allocated to registers ;size:1
;@ramInitial Flag_Led3                 Allocated to registers ;size:1
;@ramInitial Flag_Led4                 Allocated to registers ;size:1
;@ramInitial U_Flage1                  Allocated to registers ;size:1
;@ramInitial r_g_workMod               Allocated to registers ;size:1
;@ramInitial reg_2ms                   Allocated to registers ;size:1
;@ramInitial RSR                       Allocated to registers ;size:1
;@ramInitial PCH                       Allocated to registers ;size:1
;@ramInitial PCL                       Allocated to registers ;size:1
;@ramInitial STATUS                    Allocated to registers ;size:1
;@ramInitial TC0CON                    Allocated to registers ;size:1
;@ramInitial TC0C                      Allocated to registers ;size:1
;@ramInitial TBRDH                     Allocated to registers ;size:1
;@ramInitial TBRDL                     Allocated to registers ;size:1
;@ramInitial CPUCON                    Allocated to registers ;size:1
;@ramInitial IHRCCAL                   Allocated to registers ;size:1
;@ramInitial PORT5                     Allocated to registers ;size:1
;@ramInitial PORT6                     Allocated to registers ;size:1
;@ramInitial P5CON                     Allocated to registers ;size:1
;@ramInitial P6CON                     Allocated to registers ;size:1
;@ramInitial P5PH                      Allocated to registers ;size:1
;@ramInitial P6PH                      Allocated to registers ;size:1
;@ramInitial P5PD                      Allocated to registers ;size:1
;@ramInitial P6PD                      Allocated to registers ;size:1
;@ramInitial P6OD                      Allocated to registers ;size:1
;@ramInitial P6WD                      Allocated to registers ;size:1
;@ramInitial P5IWE                     Allocated to registers ;size:1
;@ramInitial P6IWE                     Allocated to registers ;size:1
;@ramInitial P5ADE                     Allocated to registers ;size:1
;@ramInitial P6ADE                     Allocated to registers ;size:1
;@ramInitial ADATH                     Allocated to registers ;size:1
;@ramInitial ADATL                     Allocated to registers ;size:1
;@ramInitial ADIS                      Allocated to registers ;size:1
;@ramInitial ADCON0                    Allocated to registers ;size:1
;@ramInitial ADCON1                    Allocated to registers ;size:1
;@ramInitial WDTCON                    Allocated to registers ;size:1
;@ramInitial TC1CON                    Allocated to registers ;size:1
;@ramInitial TC1PRDL                   Allocated to registers ;size:1
;@ramInitial PWM1DTL                   Allocated to registers ;size:1
;@ramInitial TC1PRDTH                  Allocated to registers ;size:1
;@ramInitial TC1CH                     Allocated to registers ;size:1
;@ramInitial TC1CL                     Allocated to registers ;size:1
;@ramInitial TC2CON                    Allocated to registers ;size:1
;@ramInitial TC2PRDL                   Allocated to registers ;size:1
;@ramInitial PWM2DTL                   Allocated to registers ;size:1
;@ramInitial TC2PRDTH                  Allocated to registers ;size:1
;@ramInitial TC2CH                     Allocated to registers ;size:1
;@ramInitial TC2CL                     Allocated to registers ;size:1
;@ramInitial PWM3DTH                   Allocated to registers ;size:1
;@ramInitial PWM3DTL                   Allocated to registers ;size:1
;@ramInitial PWM4DTH                   Allocated to registers ;size:1
;@ramInitial PWM4DTL                   Allocated to registers ;size:1
;@ramInitial PWMIS                     Allocated to registers ;size:1
;@ramInitial DEADCON                   Allocated to registers ;size:1
;@ramInitial PWMCON                    Allocated to registers ;size:1
;@ramInitial DEADT0                    Allocated to registers ;size:1
;@ramInitial DEADT1                    Allocated to registers ;size:1
;@ramInitial INTE0                     Allocated to registers ;size:1
;@ramInitial INTE1                     Allocated to registers ;size:1
;@ramInitial INTF0                     Allocated to registers ;size:1
;@ramInitial INTF1                     Allocated to registers ;size:1
;@ramInitial IAR                       Allocated to registers ;size:1
;@end Allocation info for local variables in function 'ramInitial';

;--------------------------------------------------------
; overlayable items in internal ram 
;--------------------------------------------------------
;	udata_ovr
;--------------------------------------------------------
; code
;--------------------------------------------------------
code_USER	code
;***
;  pBlock Stats: dbName = C
;***
;has an exit
;; Starting pCode block
S_USER__systemInit	code
_systemInit:	;Function start
; 2 exit points
;	.line	19; C:\USERS\ADMINISTRATOR\DESKTOP\培训期项目\抄板2\01_J2615_C\USER.C	WDTCON=0x00;
	CLR	_WDTCON
;	.line	22; C:\USERS\ADMINISTRATOR\DESKTOP\培训期项目\抄板2\01_J2615_C\USER.C	PORT5=0x00;
	CLR	_PORT5
;	.line	23; C:\USERS\ADMINISTRATOR\DESKTOP\培训期项目\抄板2\01_J2615_C\USER.C	PORT6=0x00;
	CLR	_PORT6
;	.line	25; C:\USERS\ADMINISTRATOR\DESKTOP\培训期项目\抄板2\01_J2615_C\USER.C	P5CON=0x00;			//P5端口控制	;0输出，1输入
	CLR	_P5CON
;	.line	26; C:\USERS\ADMINISTRATOR\DESKTOP\培训期项目\抄板2\01_J2615_C\USER.C	P6CON=0x00;			//P6端口控制    ;0输出，1输入
	CLR	_P6CON
;	.line	28; C:\USERS\ADMINISTRATOR\DESKTOP\培训期项目\抄板2\01_J2615_C\USER.C	P5PH=0xFF;			//P5口上拉		;0使能，1禁止
	MOV	A,@0xff
	MOV	_P5PH,A
;	.line	29; C:\USERS\ADMINISTRATOR\DESKTOP\培训期项目\抄板2\01_J2615_C\USER.C	P6PH=0xFF;			//P6口上拉		;0使能，1禁止
	MOV	A,@0xff
	MOV	_P6PH,A
;	.line	31; C:\USERS\ADMINISTRATOR\DESKTOP\培训期项目\抄板2\01_J2615_C\USER.C	P5PD=0xff;			//P5口下拉		;0使能，1禁止
	MOV	A,@0xff
	MOV	_P5PD,A
;	.line	32; C:\USERS\ADMINISTRATOR\DESKTOP\培训期项目\抄板2\01_J2615_C\USER.C	P6PD=0xff;			//P6口下拉		;0使能，1禁止	
	MOV	A,@0xff
	MOV	_P6PD,A
;	.line	34; C:\USERS\ADMINISTRATOR\DESKTOP\培训期项目\抄板2\01_J2615_C\USER.C	P6OD=0x00;			//P6口开漏		;0禁止，1使能
	CLR	_P6OD
;	.line	35; C:\USERS\ADMINISTRATOR\DESKTOP\培训期项目\抄板2\01_J2615_C\USER.C	P6WD=0x00;			//P6口弱驱动   ;0禁止，1使能	
	CLR	_P6WD
;	.line	38; C:\USERS\ADMINISTRATOR\DESKTOP\培训期项目\抄板2\01_J2615_C\USER.C	P5IWE=0X00;			//P5口状态变化唤醒使能
	CLR	_P5IWE
;	.line	39; C:\USERS\ADMINISTRATOR\DESKTOP\培训期项目\抄板2\01_J2615_C\USER.C	P6IWE=0X00;			//P6口状态变化唤醒使能
	CLR	_P6IWE
;	.line	42; C:\USERS\ADMINISTRATOR\DESKTOP\培训期项目\抄板2\01_J2615_C\USER.C	WDTCON=0x00;		//bit6&5:P60&P53外部中断功能控制位，0:普通IO口, 1:外部中断口
	CLR	_WDTCON
;	.line	44; C:\USERS\ADMINISTRATOR\DESKTOP\培训期项目\抄板2\01_J2615_C\USER.C	INTE0=0x01;			//中断使能 21
	MOV	A,@0x01
	MOV	_INTE0,A
;	.line	45; C:\USERS\ADMINISTRATOR\DESKTOP\培训期项目\抄板2\01_J2615_C\USER.C	INTE1=0x00;			//周期及占空比中断
	CLR	_INTE1
;	.line	46; C:\USERS\ADMINISTRATOR\DESKTOP\培训期项目\抄板2\01_J2615_C\USER.C	INTF0=0x00;			//清中断标志位
	CLR	_INTF0
;	.line	47; C:\USERS\ADMINISTRATOR\DESKTOP\培训期项目\抄板2\01_J2615_C\USER.C	INTF1=0x00;		
	CLR	_INTF1
;	.line	49; C:\USERS\ADMINISTRATOR\DESKTOP\培训期项目\抄板2\01_J2615_C\USER.C	}
	RET	
; exit point of _systemInit

;***
;  pBlock Stats: dbName = C
;***
;has an exit
;; Starting pCode block
S_USER__ramInitial	code
_ramInitial:	;Function start
; 2 exit points
;	.line	8; C:\USERS\ADMINISTRATOR\DESKTOP\培训期项目\抄板2\01_J2615_C\USER.C	for(RSR=0x80;RSR<0xff;RSR++)	//RAM清零
	MOV	A,@0x80
	MOV	_RSR,A
_00107_DS_:
	MOV	A,@0xff
	SUB	A,_RSR
	JBTC	STATUS,0
	JMP	_00105_DS_
;	.line	9; C:\USERS\ADMINISTRATOR\DESKTOP\培训期项目\抄板2\01_J2615_C\USER.C	{IAR = 0;}
	CLR	_IAR
;	.line	8; C:\USERS\ADMINISTRATOR\DESKTOP\培训期项目\抄板2\01_J2615_C\USER.C	for(RSR=0x80;RSR<0xff;RSR++)	//RAM清零
	INC	_RSR
	JMP	_00107_DS_
_00105_DS_:
;	.line	10; C:\USERS\ADMINISTRATOR\DESKTOP\培训期项目\抄板2\01_J2615_C\USER.C	IAR = 0;		
	CLR	_IAR
;	.line	11; C:\USERS\ADMINISTRATOR\DESKTOP\培训期项目\抄板2\01_J2615_C\USER.C	}
	RET	
; exit point of _ramInitial


;	code size estimation:
;	   35+    0 =    35 instructions (   70 byte)

	end
