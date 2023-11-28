package com.example.myapplication

import ApiService
import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.myapplication.databinding.ActivityMainBinding
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

class MainActivity : AppCompatActivity() {
    lateinit var binding: ActivityMainBinding

    private val retrofit = Retrofit.Builder()
        .baseUrl("https://dummyjson.com/")
        .addConverterFactory(GsonConverterFactory.create())
        .build()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val userLogin: EditText = findViewById(R.id.text_edit_login)
        val userPassword: EditText = findViewById(R.id.text_edit_password)
        val userPassword2: EditText = findViewById(R.id.text_edit_password_aggain)
        val button_log: Button = findViewById(R.id.button_goto_login)

        binding.buttonSignUp.setOnClickListener {
            val username = userLogin.text.toString().trim()
            val password = userPassword.text.toString().trim()
            val password2 = userPassword2.text.toString().trim()
            //username":"atuny0","password":"9uQFF1Lh"
            if (username.isEmpty() || password.isEmpty()) {
                Toast.makeText(this, "Not all fields are filled in", Toast.LENGTH_LONG).show()
            } else if (password != password2) {
                Toast.makeText(this, "The entered passwords must match", Toast.LENGTH_LONG).show()
            } else {
                val userAPI = retrofit.create(ApiService::class.java)
                val user = UserData(username, password)
                CoroutineScope(Dispatchers.IO).launch {
                    val response = userAPI.checkUserExists(user)
                    runOnUiThread {
                        if (response.isExecuted) {
                            Toast.makeText(this@MainActivity, "User $username is already registered", Toast.LENGTH_LONG).show()
//                            val intent = Intent(this@MainActivity, AuthActivity::class.java)
//                            startActivity(intent)
                        } else {
                            val db = DBHelper(this@MainActivity, null)
                            db.addNewUser(user)
                            Toast.makeText(this@MainActivity, "User $username is registered", Toast.LENGTH_LONG).show()
                        }
                    }
                }
            }
        }

        button_log.setOnClickListener{
            val intent = Intent(this, AuthActivity::class.java)
            startActivity(intent)
        }
    }
}

