;--------------------------------------------------------
; File Created by SLCC : free open source ANSI-C Compiler
; Version 3.6.0 #Sep 28 2025 (MSVC)
;--------------------------------------------------------
; SL port for the RISC core
;--------------------------------------------------------
;	.file	"D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C"
	list	p=JZ8P1521
	radix dec
	include "JZ8P1521.inc"
;--------------------------------------------------------
; external declarations
;--------------------------------------------------------
	extern	_fw_sleepEvent
	extern	_keyScan
	extern	_keyProcess
	extern	_fw_clrRam
	extern	_fw_gpioInit
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
	global	_fw_pwm3Init
	global	_fw_pwm2Init
	global	_fw_pwm1Init
	global	_fw_tc0Init

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

;@Allocation info for local variables in function 'fw_tc0Init'
;@fw_tc0Init fw_sleepEvent             Allocated to registers ;size:2
;@fw_tc0Init keyScan                   Allocated to registers ;size:2
;@fw_tc0Init keyProcess                Allocated to registers ;size:2
;@fw_tc0Init fw_clrRam                 Allocated to registers ;size:2
;@fw_tc0Init fw_gpioInit               Allocated to registers ;size:2
;@fw_tc0Init fw_pwm1Init               Allocated to registers ;size:2
;@fw_tc0Init fw_pwm2Init               Allocated to registers ;size:2
;@fw_tc0Init fw_pwm3Init               Allocated to registers ;size:2
;@fw_tc0Init IARbits                   Allocated to registers ;size:1
;@fw_tc0Init TCCbits                   Allocated to registers ;size:1
;@fw_tc0Init PCLbits                   Allocated to registers ;size:1
;@fw_tc0Init STATUSbits                Allocated to registers ;size:1
;@fw_tc0Init RSRbits                   Allocated to registers ;size:1
;@fw_tc0Init PORT5bits                 Allocated to registers ;size:1
;@fw_tc0Init PORT6bits                 Allocated to registers ;size:1
;@fw_tc0Init LVDCONbits                Allocated to registers ;size:1
;@fw_tc0Init PWMCONbits                Allocated to registers ;size:1
;@fw_tc0Init PRDbits                   Allocated to registers ;size:1
;@fw_tc0Init PDC1bits                  Allocated to registers ;size:1
;@fw_tc0Init PDC2bits                  Allocated to registers ;size:1
;@fw_tc0Init PDC3bits                  Allocated to registers ;size:1
;@fw_tc0Init ICIECRbits                Allocated to registers ;size:1
;@fw_tc0Init CPUCONbits                Allocated to registers ;size:1
;@fw_tc0Init ISRbits                   Allocated to registers ;size:1
;@fw_tc0Init U_Flage                   Allocated to registers ;size:1
;@fw_tc0Init r_g_workMod               Allocated to registers ;size:1
;@fw_tc0Init IAR                       Allocated to registers ;size:1
;@fw_tc0Init TCC                       Allocated to registers ;size:1
;@fw_tc0Init PCL                       Allocated to registers ;size:1
;@fw_tc0Init STATUS                    Allocated to registers ;size:1
;@fw_tc0Init RSR                       Allocated to registers ;size:1
;@fw_tc0Init PORT5                     Allocated to registers ;size:1
;@fw_tc0Init PORT6                     Allocated to registers ;size:1
;@fw_tc0Init LVDCON                    Allocated to registers ;size:1
;@fw_tc0Init PWMCON                    Allocated to registers ;size:1
;@fw_tc0Init PRD                       Allocated to registers ;size:1
;@fw_tc0Init PDC1                      Allocated to registers ;size:1
;@fw_tc0Init PDC2                      Allocated to registers ;size:1
;@fw_tc0Init PDC3                      Allocated to registers ;size:1
;@fw_tc0Init ICIECR                    Allocated to registers ;size:1
;@fw_tc0Init CPUCON                    Allocated to registers ;size:1
;@fw_tc0Init ISR                       Allocated to registers ;size:1
;@end Allocation info for local variables in function 'fw_tc0Init';

;--------------------------------------------------------
; overlayable items in internal ram 
;--------------------------------------------------------
;	udata_ovr
;--------------------------------------------------------
; code
;--------------------------------------------------------
code_FW_TIME	code
;***
;  pBlock Stats: dbName = C
;***
;has an exit
;; Starting pCode block
S_FW_TIME__fw_pwm3Init	code
_fw_pwm3Init:	;Function start
; 2 exit points
;	.line	56; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	PWMCON |= 0x80;
	BTS	_PWMCON,7
;	.line	58; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	PWMCON |= 0x40;
	BTS	_PWMCON,6
;	.line	60; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	CPUCON = 0; //bit7:IPWM1-PWM互补输出 1：pwm取反 bit6:时钟源选择1：系统时钟0：指令时钟 bit4:PWMWE-PWM 唤醒 1:PWM 唤醒使能，可唤?芽障心Ｊ?
	CLR	_CPUCON
;	.line	62; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	PRD = 100;		//PWM周期
	MOV	A,@0x64
	MOV	_PRD,A
;	.line	64; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	PDC3 = 50;		//pwmDUTY
	MOV	A,@0x32
	MOV	_PDC3,A
;	.line	66; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	IOCP_W(IMR,0X01);		//TCC中断 关闭pwm中断
	mov	a,@0X01
	iw	IMR
;	.line	68; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	ISR = 0xf7;			//清除溢出标志位
	MOV	A,@0xf7
	MOV	_ISR,A
;	.line	69; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	}
	RET	
; exit point of _fw_pwm3Init

;***
;  pBlock Stats: dbName = C
;***
;has an exit
;; Starting pCode block
S_FW_TIME__fw_pwm2Init	code
_fw_pwm2Init:	;Function start
; 2 exit points
;	.line	38; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	PWMCON |= 0x80;
	BTS	_PWMCON,7
;	.line	40; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	PWMCON |= 0x20;
	BTS	_PWMCON,5
;	.line	42; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	CPUCON = 0; //bit7:IPWM1-PWM互补输出 1：pwm取反 bit6:时钟源选择1：系统时钟0：指令时钟 bit4:PWMWE-PWM 唤醒 1:PWM 唤醒使能，可唤?芽障心Ｊ?
	CLR	_CPUCON
;	.line	44; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	PRD = 100;		//PWM周期
	MOV	A,@0x64
	MOV	_PRD,A
;	.line	46; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	PDC2 = 50;		//pwmDUTY
	MOV	A,@0x32
	MOV	_PDC2,A
;	.line	48; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	IOCP_W(IMR,0X01);		//TCC中断 关闭pwm中断
	mov	a,@0X01
	iw	IMR
;	.line	50; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	ISR = 0xf7;			//清除溢出标志位
	MOV	A,@0xf7
	MOV	_ISR,A
;	.line	51; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	}
	RET	
; exit point of _fw_pwm2Init

;***
;  pBlock Stats: dbName = C
;***
;has an exit
;; Starting pCode block
S_FW_TIME__fw_pwm1Init	code
_fw_pwm1Init:	;Function start
; 2 exit points
;	.line	20; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	PWMCON |= 0x80;
	BTS	_PWMCON,7
;	.line	22; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	PWMCON |= 0x10;
	BTS	_PWMCON,4
;	.line	25; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	CPUCON = 0; //bit7:IPWM1-PWM互补输出 1：pwm取反 bit6:时钟源选择1：系统时钟0：指令时钟 bit4:PWMWE-PWM 唤醒 1:PWM 唤醒使能，可唤?芽障心Ｊ?
	CLR	_CPUCON
;	.line	27; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	PRD = 100;		//PWM周期
	MOV	A,@0x64
	MOV	_PRD,A
;	.line	29; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	PDC1 = 50;		//pwmDUTY
	MOV	A,@0x32
	MOV	_PDC1,A
;	.line	31; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	IOCP_W(IMR,0X01);		//TCC中断 关闭pwm中断
	mov	a,@0X01
	iw	IMR
;	.line	33; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	ISR = 0xf7;			//清除溢出标志位
	MOV	A,@0xf7
	MOV	_ISR,A
;	.line	34; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	}
	RET	
; exit point of _fw_pwm1Init

;***
;  pBlock Stats: dbName = C
;***
;has an exit
;; Starting pCode block
S_FW_TIME__fw_tc0Init	code
_fw_tc0Init:	;Function start
; 2 exit points
;	.line	8; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	CONTW(0X02);			//TCC 8分频
	mov	a,@0X02
	ctw
;	.line	10; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	IOCP_W(IMR,0X01);		//TCC中断
	mov	a,@0X01
	iw	IMR
;	.line	12; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	TCC = TCC_TIM;			//1/2 * 8 * (256-6) = 1000us	鍏?寮忥拷?/IRC棰戠巼 * 棰勫垎锟??* 锟??56-鍒濆�硷級
	MOV	A,@0x06
	MOV	_TCC,A
;	.line	14; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	ISR = 0xfe;
	MOV	A,@0xfe
	MOV	_ISR,A
;	.line	15; D:\POOLBULE0\芯片代码模板\C_1521\FW_TIME.C	}
	RET	
; exit point of _fw_tc0Init


;	code size estimation:
;	   35+    0 =    35 instructions (   70 byte)

	end
