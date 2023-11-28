package com.example.myapplication

import ApiService
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast
import com.example.myapplication.databinding.ActivityAuthBinding
import com.example.myapplication.databinding.ActivityMainBinding
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

class AuthActivity : AppCompatActivity() {
    lateinit var binding: ActivityAuthBinding
    private val retrofit = Retrofit.Builder()
        .baseUrl("https://dummyjson.com/")
        .addConverterFactory(GsonConverterFactory.create())
        .build()
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_auth)

        val linkToReg: TextView = findViewById(R.id.button_goto_registration)

        val userLogin: EditText = findViewById(R.id.text_edit_login_sign_in)
        val userPassword: EditText = findViewById(R.id.text_edit_password_sign_in)

        binding = ActivityAuthBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.buttonSignUp.setOnClickListener{
            val username = userLogin.text.toString().trim()
            val password = userPassword.text.toString().trim()
            if (username.isEmpty() || password.isEmpty()) {
                Toast.makeText(this, "Not all fields are filled in", Toast.LENGTH_LONG).show()
            } else {
                val userAPI = retrofit.create(ApiService::class.java)
                val user = UserData(username, password)
                CoroutineScope(Dispatchers.IO).launch {
                    val user = userAPI.auth(user)
                }
                runOnUiThread {
                    Toast.makeText(this, "Sign in success", Toast.LENGTH_LONG).show()
                }
            }
        }

        linkToReg.setOnClickListener{
            val intent = Intent(this, MainActivity::class.java)
            startActivity(intent)
        }




    }
}