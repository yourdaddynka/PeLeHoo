import com.example.myapplication.UserData
import com.example.myapplication.retrofit.UserDataJSON
import retrofit2.Call
import retrofit2.Response
import retrofit2.http.Body
import retrofit2.http.POST

interface ApiService {
    @POST("auth/login")
    fun auth(@Body userData: UserData): UserDataJSON

    @POST("auth/login")
    fun checkUserExists(@Body userData: UserData): Call<Response<UserDataJSON>>
}
