.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static fNum F
.field static str [Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is arr [I from Label0 to Label1
.var 2 is a I from Label0 to Label1
.var 3 is b I from Label0 to Label1
.var 4 is f F from Label0 to Label1
Label0:
	iconst_4
	newarray int
	astore_1
	bipush 11
	dup
	istore_3
	dup
	istore_2
	i2f
	putstatic MCClass.fNum F
	aload_1
	iconst_0
	iload_2
	dup_x2
	iastore
	i2f
	fstore 4
	aload_1
	iconst_1
	aload_1
	iconst_0
	iload_2
	dup
	istore_3
	dup_x2
	iastore
	dup_x2
	iastore
	i2f
	putstatic MCClass.fNum F
	getstatic MCClass.fNum F
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 6
.limit locals 5
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

.method public static <clinit>()V
.limit stack 1
.limit locals 0
	iconst_4
	anewarray java/lang/String
	putstatic MCClass.str [Ljava/lang/String;
	return
.end method
