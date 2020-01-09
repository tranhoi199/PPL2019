.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a F
.field static b F
.field static c F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a Z from Label0 to Label1
.var 2 is b Z from Label0 to Label1
.var 3 is c Z from Label0 to Label1
Label0:
	iconst_1
	istore_2
	iconst_1
	istore_3
	iload_2
	ifgt Label2
	iconst_0
	ifgt Label2
	iconst_0
	goto Label3
Label2:
	iconst_1
Label3:
	ifgt Label4
	iconst_1
	iconst_0
	idiv
	ifgt Label4
	iconst_0
	goto Label5
Label4:
	iconst_1
Label5:
	istore_1
	iload_1
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 6
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
