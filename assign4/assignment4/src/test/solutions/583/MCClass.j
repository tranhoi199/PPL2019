.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a F from Label0 to Label1
.var 2 is b F from Label0 to Label1
.var 3 is gt Z from Label0 to Label1
Label0:
	ldc 2.9999
	fstore_1
	ldc 2.9998
	fstore_2
	fload_1
	fload_2
	fsub
	iconst_0
	i2f
	fcmpl
	ifle Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	istore_3
	iload_3
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 2
.limit locals 4
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
