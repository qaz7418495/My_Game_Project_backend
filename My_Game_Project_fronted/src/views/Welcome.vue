<template>
    <el-input v-model="inputusername" placeholder="Please input" clearable />
    <el-input
        v-model="inputpassword"
        type="password"
        placeholder="Please input password"
        show-password
    />
</template>

<script setup>
import {ref} from 'vue'
const inputusername = ref('')
const inputpassword = ref('')
</script>