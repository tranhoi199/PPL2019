.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static factorial(I)I
.var 0 is i I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	if_icmpgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
Label5:
	iconst_1
	ireturn
Label6:
Label4:
	iload_0
	iload_0
	iconst_1
	isub
	invokestatic MCClass/factorial(I)I
	imul
	ireturn
Label1:
.limit stack 3
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
Label0:
	bipush 10
	istore_1
	iload_1
	invokestatic MCClass/factorial(I)I
	istore_2
	iload_2
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 1
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
