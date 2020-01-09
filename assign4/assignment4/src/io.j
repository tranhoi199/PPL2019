;; Produced by JasminVisitor (BCEL)
;; http://bcel.sourceforge.net/
;; Wed Dec 04 15:43:21 ICT 2019

.source io.java
.class public io
.super java/lang/Object

.field public static input Ljava/io/BufferedReader;
.field public static writer Ljava/io/Writer;

.method public <init>()V
.limit stack 1
.limit locals 1
.var 0 is this Lio; from Label0 to Label1

Label0:
.line 9
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return

.end method

.method public static getInt()I
.limit stack 1
.limit locals 2
.var 0 is tmp Ljava/lang/String; from Label1 to Label2
.var 1 is e Ljava/lang/NumberFormatException; from Label3 to Label0
.var 1 is e Ljava/io/IOException; from Label5 to Label6

.line 23
	ldc ""
	astore_0
Label1:
.line 25
	getstatic io.input Ljava/io/BufferedReader;
	invokevirtual java/io/BufferedReader/readLine()Ljava/lang/String;
	astore_0
.line 26
	aload_0
Label8:
	invokestatic java/lang/Integer/parseInt(Ljava/lang/String;)I
	ireturn
Label9:
.line 27
	astore_1
Label5:
.line 28
	aload_1
	invokevirtual java/io/IOException/printStackTrace()V
Label6:
.line 31
	goto Label0
Label12:
.line 29
	astore_1
Label3:
.line 30
	aload_1
	invokevirtual java/lang/NumberFormatException/printStackTrace()V
Label0:
.line 32
	iconst_0
Label2:
	ireturn

.catch java/io/IOException from Label1 to Label8 using Label9
.catch java/lang/NumberFormatException from Label1 to Label8 using Label12
.end method

.method public static putInt(I)V
.limit stack 3
.limit locals 1
.var 0 is i I from Label0 to Label1

Label0:
.line 41
	getstatic java.lang.System.out Ljava/io/PrintStream;
	new java/lang/StringBuilder
	dup
	invokespecial java/lang/StringBuilder/<init>()V
	iload_0
	invokevirtual java/lang/StringBuilder/append(I)Ljava/lang/StringBuilder;
	ldc ""
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
	invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
Label1:
.line 43
	return

.end method

.method public static putIntLn(I)V
.limit stack 3
.limit locals 1
.var 0 is i I from Label0 to Label1

Label0:
.line 49
	getstatic java.lang.System.out Ljava/io/PrintStream;
	new java/lang/StringBuilder
	dup
	invokespecial java/lang/StringBuilder/<init>()V
	iload_0
	invokevirtual java/lang/StringBuilder/append(I)Ljava/lang/StringBuilder;
	ldc ""
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
	invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
Label1:
.line 50
	return

.end method

.method public static getFloat()F
.limit stack 1
.limit locals 2
.var 0 is tmp Ljava/lang/String; from Label1 to Label2
.var 1 is e Ljava/lang/NumberFormatException; from Label3 to Label0
.var 1 is e Ljava/io/IOException; from Label5 to Label6

.line 56
	ldc ""
	astore_0
Label1:
.line 58
	getstatic io.input Ljava/io/BufferedReader;
	invokevirtual java/io/BufferedReader/readLine()Ljava/lang/String;
	astore_0
.line 59
	aload_0
Label8:
	invokestatic java/lang/Float/parseFloat(Ljava/lang/String;)F
	freturn
Label9:
.line 61
	astore_1
Label5:
.line 62
	aload_1
	invokevirtual java/io/IOException/printStackTrace()V
Label6:
.line 66
	goto Label0
Label12:
.line 64
	astore_1
Label3:
.line 65
	aload_1
	invokevirtual java/lang/NumberFormatException/printStackTrace()V
Label0:
.line 67
	fconst_0
Label2:
	freturn

.catch java/io/IOException from Label1 to Label8 using Label9
.catch java/lang/NumberFormatException from Label1 to Label8 using Label12
.end method

.method public static putFloat(F)V
.limit stack 3
.limit locals 1
.var 0 is f F from Label0 to Label1

Label0:
.line 74
	getstatic java.lang.System.out Ljava/io/PrintStream;
	new java/lang/StringBuilder
	dup
	invokespecial java/lang/StringBuilder/<init>()V
	fload_0
	invokevirtual java/lang/StringBuilder/append(F)Ljava/lang/StringBuilder;
	ldc ""
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
	invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
Label1:
.line 75
	return

.end method

.method public static putFloatLn(F)V
.limit stack 3
.limit locals 1
.var 0 is f F from Label0 to Label1

Label0:
.line 81
	getstatic java.lang.System.out Ljava/io/PrintStream;
	new java/lang/StringBuilder
	dup
	invokespecial java/lang/StringBuilder/<init>()V
	fload_0
	invokevirtual java/lang/StringBuilder/append(F)Ljava/lang/StringBuilder;
	ldc ""
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
	invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
Label1:
.line 82
	return

.end method

.method public static getBool()Z
.limit stack 2
.limit locals 2
.var 0 is tmp Ljava/lang/String; from Label1 to Label2
.var 1 is e Ljava/io/IOException; from Label3 to Label4

.line 88
	ldc ""
	astore_0
Label1:
.line 90
	getstatic io.input Ljava/io/BufferedReader;
	invokevirtual java/io/BufferedReader/readLine()Ljava/lang/String;
	astore_0
.line 91
	aload_0
	ldc "true"
	invokevirtual java/lang/String/equalsIgnoreCase(Ljava/lang/String;)Z
	ifeq Label0
Label6:
.line 92
	iconst_1
	ireturn
Label0:
.line 94
	iconst_0
	ireturn
Label7:
.line 96
	astore_1
Label3:
.line 97
	aload_1
	invokevirtual java/io/IOException/printStackTrace()V
Label4:
.line 99
	iconst_0
Label2:
	ireturn

.catch java/io/IOException from Label1 to Label6 using Label7
.catch java/io/IOException from Label0 to Label0 using Label7
.end method

.method public static putBool(Z)V
.limit stack 3
.limit locals 1
.var 0 is b Z from Label0 to Label1

Label0:
.line 106
	getstatic java.lang.System.out Ljava/io/PrintStream;
	new java/lang/StringBuilder
	dup
	invokespecial java/lang/StringBuilder/<init>()V
	iload_0
	invokevirtual java/lang/StringBuilder/append(Z)Ljava/lang/StringBuilder;
	ldc ""
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
	invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
Label1:
.line 107
	return

.end method

.method public static putBoolLn(Z)V
.limit stack 3
.limit locals 1
.var 0 is b Z from Label0 to Label1

Label0:
.line 113
	getstatic java.lang.System.out Ljava/io/PrintStream;
	new java/lang/StringBuilder
	dup
	invokespecial java/lang/StringBuilder/<init>()V
	iload_0
	invokevirtual java/lang/StringBuilder/append(Z)Ljava/lang/StringBuilder;
	ldc ""
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
	invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
Label1:
.line 114
	return

.end method

.method public static putString(Ljava/lang/String;)V
.limit stack 2
.limit locals 1
.var 0 is a Ljava/lang/String; from Label0 to Label1

Label0:
.line 133
	getstatic java.lang.System.out Ljava/io/PrintStream;
	aload_0
	invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
Label1:
.line 134
	return

.end method

.method public static putStringLn(Ljava/lang/String;)V
.limit stack 2
.limit locals 1
.var 0 is a Ljava/lang/String; from Label0 to Label1

Label0:
.line 140
	getstatic java.lang.System.out Ljava/io/PrintStream;
	aload_0
	invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
Label1:
.line 141
	return

.end method

.method public static putLn()V
.limit stack 1
.limit locals 0

.line 145
	getstatic java.lang.System.out Ljava/io/PrintStream;
	invokevirtual java/io/PrintStream/println()V
.line 146
	return

.end method

.method public static close()V
.limit stack 1
.limit locals 1
.var 0 is e Ljava/io/IOException; from Label1 to Label0

Label3:
.line 150
	getstatic io.writer Ljava/io/Writer;
Label4:
	invokevirtual java/io/Writer/close()V
.line 153
	goto Label0
Label5:
.line 151
	astore_0
Label1:
.line 152
	aload_0
	invokevirtual java/io/IOException/printStackTrace()V
Label0:
.line 154
	return

.catch java/io/IOException from Label3 to Label4 using Label5
.end method

.method static <clinit>()V
.limit stack 5
.limit locals 0

.line 11
	new java/io/BufferedReader
	dup
	new java/io/InputStreamReader
	dup
	getstatic java.lang.System.in Ljava/io/InputStream;
	invokespecial java/io/InputStreamReader/<init>(Ljava/io/InputStream;)V
	invokespecial java/io/BufferedReader/<init>(Ljava/io/Reader;)V
	putstatic io.input Ljava/io/BufferedReader;
.line 12
	new java/io/BufferedWriter
	dup
	new java/io/OutputStreamWriter
	dup
	getstatic java.lang.System.out Ljava/io/PrintStream;
	invokespecial java/io/OutputStreamWriter/<init>(Ljava/io/OutputStream;)V
	invokespecial java/io/BufferedWriter/<init>(Ljava/io/Writer;)V
	putstatic io.writer Ljava/io/Writer;
	return

.end method
