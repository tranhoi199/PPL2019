.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b F
.field static f [F
.field static array [I
.field static arrayString [Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label1:
	return
.limit stack 0
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
	bipush 10
	newarray float
	putstatic MCClass.f [F
	bipush 10
	newarray int
	putstatic MCClass.array [I
	bipush 10
	anewarray java/lang/String
	putstatic MCClass.arrayString [Ljava/lang/String;
	return
.end method
