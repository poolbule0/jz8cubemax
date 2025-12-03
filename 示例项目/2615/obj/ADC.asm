;--------------------------------------------------------
; File Created by SLCC : free open source ANSI-C Compiler
; Version 3.6.0 #Sep 28 2025 (MSVC)
;--------------------------------------------------------
; SL port for the RISC core
;--------------------------------------------------------
;	.file	"C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ADC.C"
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
	global	_ADC_GetValue
	global	_ADC_value

;--------------------------------------------------------
; global definitions
;--------------------------------------------------------
UD_ADC_0	udata
_ADC_value	res	2

;--------------------------------------------------------
; absolute symbol definitions
;--------------------------------------------------------
;--------------------------------------------------------
; compiler-defined variables
;--------------------------------------------------------
UDL_ADC_0	udata
r0x1002	res	1
r0x1003	res	1
r0x1004	res	1
r0x1005	res	1
r0x1006	res	1
r0x1007	res	1
r0x1008	res	1
r0x1009	res	1
r0x100A	res	1
r0x100B	res	1
r0x100C	res	1
r0x100D	res	1
r0x100E	res	1
r0x100F	res	1
r0x1010	res	1
;--------------------------------------------------------
; initialized data
;--------------------------------------------------------

;@Allocation info for local variables in function 'ADC_GetValue'
;@ADC_GetValue RSRbits                   Allocated to registers ;size:1
;@ADC_GetValue PCHbits                   Allocated to registers ;size:1
;@ADC_GetValue PCLbits                   Allocated to registers ;size:1
;@ADC_GetValue STATUSbits                Allocated to registers ;size:1
;@ADC_GetValue TC0CONbits                Allocated to registers ;size:1
;@ADC_GetValue TC0Cbits                  Allocated to registers ;size:1
;@ADC_GetValue TBRDHbits                 Allocated to registers ;size:1
;@ADC_GetValue TBRDLbits                 Allocated to registers ;size:1
;@ADC_GetValue CPUCONbits                Allocated to registers ;size:1
;@ADC_GetValue IHRCCALbits               Allocated to registers ;size:1
;@ADC_GetValue PORT5bits                 Allocated to registers ;size:1
;@ADC_GetValue PORT6bits                 Allocated to registers ;size:1
;@ADC_GetValue P5CONbits                 Allocated to registers ;size:1
;@ADC_GetValue P6CONbits                 Allocated to registers ;size:1
;@ADC_GetValue P5PHbits                  Allocated to registers ;size:1
;@ADC_GetValue P6PHbits                  Allocated to registers ;size:1
;@ADC_GetValue P5PDbits                  Allocated to registers ;size:1
;@ADC_GetValue P6PDbits                  Allocated to registers ;size:1
;@ADC_GetValue P6ODbits                  Allocated to registers ;size:1
;@ADC_GetValue P6WDbits                  Allocated to registers ;size:1
;@ADC_GetValue P5IWEbits                 Allocated to registers ;size:1
;@ADC_GetValue P6IWEbits                 Allocated to registers ;size:1
;@ADC_GetValue P5ADEbits                 Allocated to registers ;size:1
;@ADC_GetValue P6ADEbits                 Allocated to registers ;size:1
;@ADC_GetValue ADATHbits                 Allocated to registers ;size:1
;@ADC_GetValue ADATLbits                 Allocated to registers ;size:1
;@ADC_GetValue ADISbits                  Allocated to registers ;size:1
;@ADC_GetValue ADCON0bits                Allocated to registers ;size:1
;@ADC_GetValue ADCON1bits                Allocated to registers ;size:1
;@ADC_GetValue WDTCONbits                Allocated to registers ;size:1
;@ADC_GetValue TC1CONbits                Allocated to registers ;size:1
;@ADC_GetValue TC1PRDLbits               Allocated to registers ;size:1
;@ADC_GetValue PWM1DTLbits               Allocated to registers ;size:1
;@ADC_GetValue TC1PRDTHbits              Allocated to registers ;size:1
;@ADC_GetValue TC1CHbits                 Allocated to registers ;size:1
;@ADC_GetValue TC1CLbits                 Allocated to registers ;size:1
;@ADC_GetValue TC2CONbits                Allocated to registers ;size:1
;@ADC_GetValue TC2PRDLbits               Allocated to registers ;size:1
;@ADC_GetValue PWM2DTLbits               Allocated to registers ;size:1
;@ADC_GetValue TC2PRDTHbits              Allocated to registers ;size:1
;@ADC_GetValue TC2CHbits                 Allocated to registers ;size:1
;@ADC_GetValue TC2CLbits                 Allocated to registers ;size:1
;@ADC_GetValue PWM3DTHbits               Allocated to registers ;size:1
;@ADC_GetValue PWM3DTLbits               Allocated to registers ;size:1
;@ADC_GetValue PWM4DTHbits               Allocated to registers ;size:1
;@ADC_GetValue PWM4DTLbits               Allocated to registers ;size:1
;@ADC_GetValue PWMISbits                 Allocated to registers ;size:1
;@ADC_GetValue DEADCONbits               Allocated to registers ;size:1
;@ADC_GetValue PWMCONbits                Allocated to registers ;size:1
;@ADC_GetValue DEADT0bits                Allocated to registers ;size:1
;@ADC_GetValue DEADT1bits                Allocated to registers ;size:1
;@ADC_GetValue INTE0bits                 Allocated to registers ;size:1
;@ADC_GetValue INTE1bits                 Allocated to registers ;size:1
;@ADC_GetValue INTF0bits                 Allocated to registers ;size:1
;@ADC_GetValue INTF1bits                 Allocated to registers ;size:1
;@ADC_GetValue IARbits                   Allocated to registers ;size:1
;@ADC_GetValue U_Flage1                  Allocated to registers ;size:1
;@ADC_GetValue r_g_workMod               Allocated to registers ;size:1
;@ADC_GetValue ADC_value                 Allocated to registers ;size:2
;@ADC_GetValue vref                      Allocated to registers r0x1003 ;size:1
;@ADC_GetValue chn                       Allocated to registers r0x1002 ;size:1
;@ADC_GetValue delay_time                Allocated to registers r0x1003 r0x100C ;size:2
;@ADC_GetValue ADC_value_high            Allocated to registers r0x1004 r0x1005 ;size:2
;@ADC_GetValue ADC_value_low             Allocated to registers r0x1006 r0x1007 ;size:2
;@ADC_GetValue ADC_value_sum             Allocated to registers r0x1008 r0x1009 r0x100A r0x100B ;size:4
;@ADC_GetValue count                     Allocated to registers r0x1002 ;size:1
;@ADC_GetValue RSR                       Allocated to registers ;size:1
;@ADC_GetValue PCH                       Allocated to registers ;size:1
;@ADC_GetValue PCL                       Allocated to registers ;size:1
;@ADC_GetValue STATUS                    Allocated to registers ;size:1
;@ADC_GetValue TC0CON                    Allocated to registers ;size:1
;@ADC_GetValue TC0C                      Allocated to registers ;size:1
;@ADC_GetValue TBRDH                     Allocated to registers ;size:1
;@ADC_GetValue TBRDL                     Allocated to registers ;size:1
;@ADC_GetValue CPUCON                    Allocated to registers ;size:1
;@ADC_GetValue IHRCCAL                   Allocated to registers ;size:1
;@ADC_GetValue PORT5                     Allocated to registers ;size:1
;@ADC_GetValue PORT6                     Allocated to registers ;size:1
;@ADC_GetValue P5CON                     Allocated to registers ;size:1
;@ADC_GetValue P6CON                     Allocated to registers ;size:1
;@ADC_GetValue P5PH                      Allocated to registers ;size:1
;@ADC_GetValue P6PH                      Allocated to registers ;size:1
;@ADC_GetValue P5PD                      Allocated to registers ;size:1
;@ADC_GetValue P6PD                      Allocated to registers ;size:1
;@ADC_GetValue P6OD                      Allocated to registers ;size:1
;@ADC_GetValue P6WD                      Allocated to registers ;size:1
;@ADC_GetValue P5IWE                     Allocated to registers ;size:1
;@ADC_GetValue P6IWE                     Allocated to registers ;size:1
;@ADC_GetValue P5ADE                     Allocated to registers ;size:1
;@ADC_GetValue P6ADE                     Allocated to registers ;size:1
;@ADC_GetValue ADATH                     Allocated to registers ;size:1
;@ADC_GetValue ADATL                     Allocated to registers ;size:1
;@ADC_GetValue ADIS                      Allocated to registers ;size:1
;@ADC_GetValue ADCON0                    Allocated to registers ;size:1
;@ADC_GetValue ADCON1                    Allocated to registers ;size:1
;@ADC_GetValue WDTCON                    Allocated to registers ;size:1
;@ADC_GetValue TC1CON                    Allocated to registers ;size:1
;@ADC_GetValue TC1PRDL                   Allocated to registers ;size:1
;@ADC_GetValue PWM1DTL                   Allocated to registers ;size:1
;@ADC_GetValue TC1PRDTH                  Allocated to registers ;size:1
;@ADC_GetValue TC1CH                     Allocated to registers ;size:1
;@ADC_GetValue TC1CL                     Allocated to registers ;size:1
;@ADC_GetValue TC2CON                    Allocated to registers ;size:1
;@ADC_GetValue TC2PRDL                   Allocated to registers ;size:1
;@ADC_GetValue PWM2DTL                   Allocated to registers ;size:1
;@ADC_GetValue TC2PRDTH                  Allocated to registers ;size:1
;@ADC_GetValue TC2CH                     Allocated to registers ;size:1
;@ADC_GetValue TC2CL                     Allocated to registers ;size:1
;@ADC_GetValue PWM3DTH                   Allocated to registers ;size:1
;@ADC_GetValue PWM3DTL                   Allocated to registers ;size:1
;@ADC_GetValue PWM4DTH                   Allocated to registers ;size:1
;@ADC_GetValue PWM4DTL                   Allocated to registers ;size:1
;@ADC_GetValue PWMIS                     Allocated to registers ;size:1
;@ADC_GetValue DEADCON                   Allocated to registers ;size:1
;@ADC_GetValue PWMCON                    Allocated to registers ;size:1
;@ADC_GetValue DEADT0                    Allocated to registers ;size:1
;@ADC_GetValue DEADT1                    Allocated to registers ;size:1
;@ADC_GetValue INTE0                     Allocated to registers ;size:1
;@ADC_GetValue INTE1                     Allocated to registers ;size:1
;@ADC_GetValue INTF0                     Allocated to registers ;size:1
;@ADC_GetValue INTF1                     Allocated to registers ;size:1
;@ADC_GetValue IAR                       Allocated to registers ;size:1
;@end Allocation info for local variables in function 'ADC_GetValue';

;--------------------------------------------------------
; overlayable items in internal ram 
;--------------------------------------------------------
;	udata_ovr
;--------------------------------------------------------
; code
;--------------------------------------------------------
code_ADC	code
;***
;  pBlock Stats: dbName = C
;***
;has an exit
;16 compiler assigned registers:
;   r0x1002
;   STK00
;   r0x1003
;   r0x1004
;   r0x1005
;   r0x1006
;   r0x1007
;   r0x1008
;   r0x1009
;   r0x100A
;   r0x100B
;   r0x100C
;   r0x100D
;   r0x100E
;   r0x100F
;   r0x1010
;; Starting pCode block
S_ADC__ADC_GetValue	code
_ADC_GetValue:	;Function start
; 2 exit points
;	.line	5; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ADC.C	uint16_t ADC_GetValue(uint8_t chn,uint8_t vref)
	MOV	r0x1002,A
	MOV	A,STK00
	MOV	r0x1003,A
;	.line	9; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ADC.C	uint16_t ADC_value_high = 0;
	CLR	r0x1004
	CLR	r0x1005
;	.line	10; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ADC.C	uint16_t ADC_value_low = 0xffff;
	MOV	A,@0xff
	MOV	r0x1006,A
	MOV	r0x1007,A
;	.line	11; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ADC.C	uint32_t ADC_value_sum = 0;
	CLR	r0x1008
	CLR	r0x1009
	CLR	r0x100A
	CLR	r0x100B
;	.line	18; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ADC.C	ADIS = (chn << 4);		        //AD采样口使能口
	SWAPA	r0x1002
	AND	A,@0xf0
	MOV	_ADIS,A
;	.line	19; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ADC.C	ADCON0 = vref | C_Ckl_Div16;	//AD基准电压及分频选择,16分频
	MOV	A,r0x1003
	MOV	_ADCON0,A
;	.line	21; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ADC.C	ADCON1 = C_ADC_START;	//AD使能，不校准
	MOV	A,@0x40
	MOV	_ADCON1,A
;	.line	27; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ADC.C	for(count = 0; count < 10; count++)
	CLR	r0x1002
_00114_DS_:
;	.line	29; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ADC.C	ADRUN = 1;
	BTS	_ADCON1bits,7
;	.line	30; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ADC.C	delay_time = DELAY_TIME;
	MOV	A,@0xb8
	MOV	r0x1003,A
	MOV	A,@0x0b
	MOV	r0x100C,A
_00106_DS_:
;	.line	31; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ADC.C	while(ADRUN && (--delay_time));
	JBTS	_ADCON1bits,7
	JMP	_00108_DS_
	MOV	A,@0xff
	ADD	A,r0x1003
	MOV	r0x100D,A
	MOV	A,r0x100C
	JBTC	STATUS,0
	IJA	r0x100C
	ADD	A,@0xff
	MOV	r0x100C,A
	MOV	r0x100E,A
	MOV	A,r0x100D
	MOV	r0x1003,A
;;103	MOV	A,r0x100E
	MOV	A,r0x100D
	OR	A,r0x100E
	JBTS	STATUS,2
	JMP	_00106_DS_
_00108_DS_:
;	.line	33; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ADC.C	ADC_value = ADIS & 0x0f;
	MOV	A,@0x0f
	AND	A,_ADIS
	MOV	_ADC_value,A
	MOV	r0x1003,A
;;101	MOV	A,r0x1003
	CLR	(_ADC_value + 1)
;	.line	34; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ADC.C	ADC_value = (ADC_value << 8) + ADATL;
	MOV	A,_ADC_value
	MOV	r0x100C,A
	CLR	r0x1003
	MOV	A,_ADATL
	MOV	r0x100F,A
	MOV	r0x100D,A
	CLR	r0x100E
;;102	MOV	A,r0x100D
	MOV	A,@0x00
	MOV	r0x1010,A
	MOV	A,r0x100F
	ADD	A,r0x1003
	MOV	_ADC_value,A
	MOV	A,r0x100C
	MOV	(_ADC_value + 1),A
	MOV	A,r0x1010
	MOV	A,r0x1010
	JBTC	STATUS,0
	IJA	r0x1010
	ADD	(_ADC_value + 1),A
;	.line	35; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ADC.C	if(ADC_value > ADC_value_high)
	MOV	A,(_ADC_value + 1)
	SUB	A,r0x1005
	JBTS	STATUS,2
	JMP	_00137_DS_
	MOV	A,_ADC_value
	SUB	A,r0x1004
_00137_DS_:
	JBTC	STATUS,0
	JMP	_00110_DS_
;	.line	37; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ADC.C	ADC_value_high = ADC_value;
	MOV	A,_ADC_value
	MOV	r0x1004,A
	MOV	A,(_ADC_value + 1)
	MOV	r0x1005,A
_00110_DS_:
;	.line	39; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ADC.C	if(ADC_value < ADC_value_low)
	MOV	A,r0x1007
	SUB	A,(_ADC_value + 1)
	JBTS	STATUS,2
	JMP	_00138_DS_
	MOV	A,r0x1006
	SUB	A,_ADC_value
_00138_DS_:
	JBTC	STATUS,0
	JMP	_00112_DS_
;	.line	41; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ADC.C	ADC_value_low = ADC_value;
	MOV	A,_ADC_value
	MOV	r0x1006,A
	MOV	A,(_ADC_value + 1)
	MOV	r0x1007,A
_00112_DS_:
;	.line	43; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ADC.C	ADC_value_sum += ADC_value;
	MOV	A,_ADC_value
	MOV	r0x1003,A
	MOV	A,(_ADC_value + 1)
	MOV	r0x100C,A
	CLR	r0x100D
	CLR	r0x100E
	MOV	A,r0x1003
	ADD	r0x1008,A
	MOV	A,r0x100C
	MOV	A,r0x100C
	JBTC	STATUS,0
	IJA	r0x100C
	ADD	r0x1009,A
	MOV	A,r0x100D
	MOV	A,r0x100D
	JBTC	STATUS,0
	IJA	r0x100D
	ADD	r0x100A,A
	MOV	A,r0x100E
	MOV	A,r0x100E
	JBTC	STATUS,0
	IJA	r0x100E
	ADD	r0x100B,A
;	.line	27; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ADC.C	for(count = 0; count < 10; count++)
	INC	r0x1002
	MOV	A,@0x0a
	SUB	A,r0x1002
	JBTS	STATUS,0
	JMP	_00114_DS_
;;105	MOV	A,r0x1004
;	.line	46; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ADC.C	ADC_value = (ADC_value_sum - ADC_value_high - ADC_value_low + 4) >> 3;
	MOV	A,r0x1005
	MOV	r0x1003,A
	CLR	r0x100C
	CLR	r0x100D
;;104	MOV	A,r0x1002
	MOV	A,r0x1004
	MOV	r0x1002,A
	SUB	A,r0x1008
	MOV	r0x1004,A
	MOV	A,r0x1009
	MOV	r0x1005,A
	MOV	A,r0x1003
	JBTS	STATUS,0
	IJA	r0x1003
	SUB	r0x1005,A
	MOV	A,r0x100A
	MOV	r0x100E,A
	MOV	A,r0x100C
	JBTS	STATUS,0
	IJA	r0x100C
	SUB	r0x100E,A
	MOV	A,r0x100D
	JBTS	STATUS,0
	INCA	r0x100D
	SUB	A,r0x100B
	MOV	r0x100F,A
;;100	MOV	A,r0x1006
	MOV	A,r0x1007
	MOV	r0x1003,A
	CLR	r0x1008
	CLR	r0x1009
;;99	MOV	A,r0x1002
	MOV	A,r0x1006
	MOV	r0x1002,A
	SUB	A,r0x1004
	MOV	r0x1006,A
	MOV	A,r0x1005
	MOV	r0x1007,A
	MOV	A,r0x1003
	JBTS	STATUS,0
	IJA	r0x1003
	SUB	r0x1007,A
	MOV	A,r0x100E
	MOV	r0x100A,A
	MOV	A,r0x1008
	JBTS	STATUS,0
	IJA	r0x1008
	SUB	r0x100A,A
	MOV	A,r0x1009
	JBTS	STATUS,0
	INCA	r0x1009
	SUB	A,r0x100F
	MOV	r0x100B,A
	MOV	A,@0x04
	ADD	r0x1006,A
	JBTC	STATUS,0
	INC	r0x1007
	JBTC	STATUS,2
	INC	r0x100A
	JBTC	STATUS,2
	INC	r0x100B
	BTC	STATUS,0
	RCA	r0x100B
	MOV	r0x1005,A
	RCA	r0x100A
	MOV	r0x1004,A
	RCA	r0x1007
	MOV	r0x1003,A
	RCA	r0x1006
	MOV	r0x1002,A
	BTC	STATUS,0
	RCR	r0x1005
	RCR	r0x1004
	RCR	r0x1003
	RCR	r0x1002
	BTC	STATUS,0
	RCR	r0x1005
	RCR	r0x1004
	RCR	r0x1003
	RCR	r0x1002
	MOV	A,r0x1002
	MOV	_ADC_value,A
	MOV	A,r0x1003
	MOV	(_ADC_value + 1),A
;	.line	48; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ADC.C	return ADC_value;
	MOV	A,_ADC_value
	MOV	STK00,A
	MOV	A,(_ADC_value + 1)
;	.line	49; C:\USERS\ADMINISTRATOR\DESKTOP\188-PRJ\2\ADC.C	}
	RET	
; exit point of _ADC_GetValue


;	code size estimation:
;	  203+    0 =   203 instructions (  406 byte)

	end
