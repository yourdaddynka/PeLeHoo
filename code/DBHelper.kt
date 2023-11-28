package com.example.myapplication

import android.content.ContentValues
import android.content.Context
import android.database.sqlite.SQLiteDatabase
import android.database.sqlite.SQLiteOpenHelper

class DBHelper (val context: Context, val factory: SQLiteDatabase.CursorFactory?) :
    SQLiteOpenHelper(context, "DB", factory,1){
    override fun onCreate(db: SQLiteDatabase?) {
        val query = "CREATE TABLE person (id INT PRIMARY KEY, username, password)"
        db!!.execSQL(query)
    }

    override fun onUpgrade(db: SQLiteDatabase?, p1: Int, p2: Int) {
        val query = "DROP TABLE IF EXISTS person"
        db!!.execSQL(query)
        onCreate(db)
    }

    fun addNewUser(user: UserData) {
        val values = ContentValues()
        values.put("username", user.username)
        values.put("password", user.password)

        val db = this.writableDatabase
        db.insert("person", null, values)

        db.close()
    }

    fun checkIfUserExists(username: String): Boolean {
        val db = readableDatabase
        val query = "SELECT * FROM person WHERE username = '$username'"
        val cursor = db.rawQuery(query, null)
        val userExists = cursor.count > 0
        cursor.close()
        return userExists
    }

}