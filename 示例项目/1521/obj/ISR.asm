;--------------------------------------------------------
; File Created by SLCC : free open source ANSI-C Compiler
; Version 3.6.0 #Sep 28 2025 (MSVC)
;--------------------------------------------------------
; SL port for the RISC core
;--------------------------------------------------------
;	.file	"D:\POOLBULE0\芯片代码模板\C_1521\ISR.C"
	list	p=JZ8P1521
	radix dec
	include "JZ8P1521.inc"
;--------------------------------------------------------
; external declarations
;--------------------------------------------------------
	extern	_fw_pwm1Init
	extern	_fw_pwm2Init
	extern	_fw_pwm3Init
	extern	_fw_sleepEvent
	extern	_keyScan
	extern	_keyProcess
	extern	_fw_clrRam
	extern	_fw_gpioInit
	extern	_fw_tc0Init
	extern	_IARbits
	extern	_TCCbits
	extern	_PCLbits
	extern	_STATUSbits
	extern	_RSRbits
	extern	_PORT5bits
	extern	_PORT6bits
	extern	_LVDCONbits
	extern	_PWMCONbits
	extern	_PRDbits
	extern	_PDC1bits
	extern	_PDC2bits
	extern	_PDC3bits
	extern	_ICIECRbits
	extern	_CPUCONbits
	extern	_ISRbits
	extern	_U_Flage
	extern	_r_g_workMod
	extern	_IAR
	extern	_TCC
	extern	_PCL
	extern	_STATUS
	extern	_RSR
	extern	_PORT5
	extern	_PORT6
	extern	_LVDCON
	extern	_PWMCON
	extern	_PRD
	extern	_PDC1
	extern	_PDC2
	extern	_PDC3
	extern	_ICIECR
	extern	_CPUCON
	extern	_ISR

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
	global	_A_BUFF
	global	_R3_BUFF

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
UD_abs_ISR_10	udata_ovr	0x0010
_A_BUFF
	res	1
UD_abs_ISR_11	udata_ovr	0x0011
_R3_BUFF
	res	1
;--------------------------------------------------------
; compiler-defined variables
;--------------------------------------------------------
UDL_ISR_0	udata
r0x1002	res	1
;--------------------------------------------------------
; initialized data
;--------------------------------------------------------

;@Allocation info for local variables in function 'int_isr'
;@int_isr fw_pwm1Init               Allocated to registers ;size:2
;@int_isr fw_pwm2Init               Allocated to registers ;size:2
;@int_isr fw_pwm3Init               Allocated to registers ;size:2
;@int_isr fw_sleepEvent             Allocated to registers ;size:2
;@int_isr keyScan                   Allocated to registers ;size:2
;@int_isr keyProcess                Allocated to registers ;size:2
;@int_isr fw_clrRam                 Allocated to registers ;size:2
;@int_isr fw_gpioInit               Allocated to registers ;size:2
;@int_isr fw_tc0Init                Allocated to registers ;size:2
;@int_isr int_isr                   Allocated to registers ;size:2
;@int_isr IARbits                   Allocated to registers ;size:1
;@int_isr TCCbits                   Allocated to registers ;size:1
;@int_isr PCLbits                   Allocated to registers ;size:1
;@int_isr STATUSbits                Allocated to registers ;size:1
;@int_isr RSRbits                   Allocated to registers ;size:1
;@int_isr PORT5bits                 Allocated to registers ;size:1
;@int_isr PORT6bits                 Allocated to registers ;size:1
;@int_isr LVDCONbits                Allocated to registers ;size:1
;@int_isr PWMCONbits                Allocated to registers ;size:1
;@int_isr PRDbits                   Allocated to registers ;size:1
;@int_isr PDC1bits                  Allocated to registers ;size:1
;@int_isr PDC2bits                  Allocated to registers ;size:1
;@int_isr PDC3bits                  Allocated to registers ;size:1
;@int_isr ICIECRbits                Allocated to registers ;size:1
;@int_isr CPUCONbits                Allocated to registers ;size:1
;@int_isr ISRbits                   Allocated to registers ;size:1
;@int_isr U_Flage                   Allocated to registers ;size:1
;@int_isr r_g_workMod               Allocated to registers ;size:1
;@int_isr reg_200us                 Allocated to registers ;size:1
;@int_isr reg_10ms                  Allocated to registers ;size:1
;@int_isr A_BUFF                    Allocated to registers ;size:1
;@int_isr R3_BUFF                   Allocated to registers ;size:1
;@int_isr IAR                       Allocated to registers ;size:1
;@int_isr TCC                       Allocated to registers ;size:1
;@int_isr PCL                       Allocated to registers ;size:1
;@int_isr STATUS                    Allocated to registers ;size:1
;@int_isr RSR                       Allocated to registers ;size:1
;@int_isr PORT5                     Allocated to registers ;size:1
;@int_isr PORT6                     Allocated to registers ;size:1
;@int_isr LVDCON                    Allocated to registers ;size:1
;@int_isr PWMCON                    Allocated to registers ;size:1
;@int_isr PRD                       Allocated to registers ;size:1
;@int_isr PDC1                      Allocated to registers ;size:1
;@int_isr PDC2                      Allocated to registers ;size:1
;@int_isr PDC3                      Allocated to registers ;size:1
;@int_isr ICIECR                    Allocated to registers ;size:1
;@int_isr CPUCON                    Allocated to registers ;size:1
;@int_isr ISR                       Allocated to registers ;size:1
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
;2 compiler assigned registers:
;   r0x1002
;   r0x1003
;; Starting pCode block
_int_isr:	;Function start
; 0 exit points
;	.line	11; D:\POOLBULE0\芯片代码模板\C_1521\ISR.C	__asm__("org 0x08");			//中断入口地址	
	org	0x08
;	.line	12; D:\POOLBULE0\芯片代码模板\C_1521\ISR.C	DI();		
	di	
;	.line	13; D:\POOLBULE0\芯片代码模板\C_1521\ISR.C	PUSH(_A_BUFF,_R3_BUFF);			//中断入栈保护
	mov	_A_BUFF,a
	swap	_A_BUFF
	swapa	STATUS
	mov	_R3_BUFF,a
;	.line	15; D:\POOLBULE0\芯片代码模板\C_1521\ISR.C	if(TCIF == 1)					//判断TCIF是否为1
	CLR	r0x1002
	JBTC	_ISRbits,0
	INC	r0x1002
;;101	MOV	A,r0x1002
;;99	MOV	r0x1003,A
;;100	MOV	A,r0x1003
	MOV	A,r0x1002
	XOR	A,@0x01
	JBTS	STATUS,2
	JMP	_00108_DS_
;	.line	17; D:\POOLBULE0\芯片代码模板\C_1521\ISR.C	TCC += TCC_TIM;			//1/2 * 8 * (256-6) = 1000us	公式：1/IRC频率 * 预分频 * （256-初值）
	MOV	A,@0x06
	ADD	_TCC,A
;	.line	18; D:\POOLBULE0\芯片代码模板\C_1521\ISR.C	ISR = 0xfe;				//清TC0中断标志位
	MOV	A,@0xfe
	MOV	_ISR,A
;	.line	20; D:\POOLBULE0\芯片代码模板\C_1521\ISR.C	if (++ reg_10ms >= 1)
	INC	_reg_10ms
	MOV	A,@0x01
	SUB	A,_reg_10ms
	JBTS	STATUS,0
	JMP	_00108_DS_
;	.line	22; D:\POOLBULE0\芯片代码模板\C_1521\ISR.C	reg_10ms = 0;
	CLR	_reg_10ms
;	.line	23; D:\POOLBULE0\芯片代码模板\C_1521\ISR.C	Time_10ms = ENABLE;
	BTS	_U_Flage,0
_00108_DS_:
;	.line	28; D:\POOLBULE0\芯片代码模板\C_1521\ISR.C	ISR = 0x01; //清不使用的中断标志位
	MOV	A,@0x01
	MOV	_ISR,A
;	.line	29; D:\POOLBULE0\芯片代码模板\C_1521\ISR.C	POP(_A_BUFF,_R3_BUFF);			//中断出栈保护恢复
	swapa	_R3_BUFF
	mov	STATUS,a
	swapa	_A_BUFF
;	.line	30; D:\POOLBULE0\芯片代码模板\C_1521\ISR.C	EI();
	ei	
;	.line	31; D:\POOLBULE0\芯片代码模板\C_1521\ISR.C	}
END_OF_INTERRUPT:
	RETI	

;--------------------------------------------------------
; code
;--------------------------------------------------------
code_ISR	code

;	code size estimation:
;	   21+    0 =    21 instructions (   42 byte)

	end
