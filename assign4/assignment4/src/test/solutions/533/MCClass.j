.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static arr [I
.field static b [Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MCClass.b [Z
	iconst_0
	iconst_0
	bastore
	getstatic MCClass.b [Z
	iconst_0
	baload
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 4
.limit locals 1
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
	iconst_5
	newarray int
	putstatic MCClass.arr [I
	iconst_4
	newarray boolean
	putstatic MCClass.b [Z
	return
.end method
