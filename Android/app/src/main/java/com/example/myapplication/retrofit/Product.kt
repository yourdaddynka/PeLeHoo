package com.example.hackaton_example.retrofit

import java.io.FileDescriptor

data class Product(
    val id: Int,
    val title: String,
    val descriptor: String,
    val price: Int,
    val discountPercentage: Float,
    val rating: Float,
    val stock: Int,
    val brand: String,
    val category: String,
    val thumbnail: String,
    val images: List<String>
)
