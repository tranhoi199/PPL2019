.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static isTrue Z
.field static arr [Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is isT Z from Label0 to Label1
.var 2 is isF Z from Label0 to Label1
Label0:
	getstatic MCClass.arr [Z
	iconst_0
	getstatic MCClass.arr [Z
	iconst_1
	getstatic MCClass.arr [Z
	iconst_2
	iconst_0
	dup_x2
	bastore
	dup_x2
	bastore
	bastore
	getstatic MCClass.arr [Z
	iconst_0
	baload
	ifgt Label2
	iconst_0
	goto Label3
Label2:
	iconst_0
Label3:
	istore_1
	getstatic MCClass.arr [Z
	iconst_1
	baload
	ifgt Label4
	iconst_0
	goto Label5
Label4:
	iconst_0
Label5:
	ifgt Label6
	iconst_0
	goto Label7
Label6:
	iconst_0
Label7:
	istore_2
	iload_2
	ifgt Label8
	iconst_0
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
	iconst_0
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label12
	iconst_0
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label14
	iconst_0
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label16
	iconst_0
	goto Label17
Label16:
	iconst_0
Label17:
	ifgt Label18
	iconst_0
	goto Label19
Label18:
	iconst_0
Label19:
	putstatic MCClass.isTrue Z
	getstatic MCClass.isTrue Z
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 11
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

.method public static <clinit>()V
.limit stack 1
.limit locals 0
	iconst_4
	newarray boolean
	putstatic MCClass.arr [Z
	return
.end method
