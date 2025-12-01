#ifndef _TYPE_H_
#define _TYPE_H_

#include "JZ8P2615.h"



#define ei()  __asm__(" ei ")
#define di()  __asm__(" di ")
#define nop() __asm__(" nop ")
#define sleep() __asm__(" sleep ")
#define cwdt() __asm__(" cwdt ")
#define ret() __asm__(" ret ")

#define ctw(val)	        __asm__("mov a,@"#val"\n ctw")
#define iw(reg,val)		    __asm__("mov a,@"#val"\n iw "#reg)
#define ir(ram,reg)		    __asm__("ir "#reg"\n mov "#ram",a")
#define push(a_reg,R3_reg)	__asm__("mov _"#a_reg",a\n swap _"#a_reg"\n swapa STATUS\n mov _"#R3_reg",a")
#define pop(a_reg,R3_reg)	__asm__("swapa _"#R3_reg"\n mov STATUS,a\n swapa _"#a_reg)
#define rcr2(h1,l1)         __asm__("btc _STATUSbits,0\n rcr _"#h1"\n rcr _"#l1)

typedef   unsigned char		uint8_t;
typedef   unsigned int 		uint16_t;
typedef   unsigned long     uint32_t;

#define   ENABLE    1
#define   DISABLE   0

#endif /* _TYPE_H_ */