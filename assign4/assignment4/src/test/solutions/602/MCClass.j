.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
.var 3 is res I from Label0 to Label1
Label0:
	bipush 11
	istore_1
	bipush 12
	istore_2
	iload_1
	iload_2
	invokestatic MCClass/foo(II)I
	istore_3
	iload_3
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 2
.limit locals 4
.end method

.method public static foo(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_0
	iload_1
	if_icmpeq Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
Label5:
	iload_0
	iconst_1
	if_icmpeq Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label9
Label10:
	iload_0
	iconst_1
	iadd
	istore_0
Label11:
	goto Label12
Label9:
Label13:
	iload_1
	iconst_1
	if_icmpne Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifle Label17
Label18:
	iconst_1
	ireturn
Label19:
	goto Label20
Label17:
Label21:
	iload_0
	iconst_3
	iadd
	istore_0
Label22:
Label20:
Label14:
Label12:
	iload_0
	ireturn
Label6:
	goto Label23
Label4:
Label24:
	iconst_0
	ireturn
Label25:
Label23:
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public static complex(III)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is c I from Label0 to Label1
Label0:
	iload_0
	iload_1
	if_icmpeq Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
Label5:
	iload_0
	ireturn
Label6:
	goto Label7
Label4:
Label8:
	iload_2
	iload_1
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label12
Label13:
	iload_2
	ireturn
Label14:
	goto Label15
Label12:
Label16:
	iload_1
	ireturn
Label17:
Label15:
Label9:
Label7:
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
