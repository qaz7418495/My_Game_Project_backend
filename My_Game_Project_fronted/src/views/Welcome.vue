<template>
    <Header/>
    <div class="input">
        <div class="input_row">
            <span style="width: 70px; text-align: left;">用户名</span>
            <el-input class="input_u" v-model="inputusername" placeholder="Please input"/>
        </div>
        <div class="input_row" style="margin-left: 20px;">
            <span style="width: 70px; text-align: left;">密码</span>
            <el-input
                class="input_p"
                v-model="inputpassword"
                type="password"
                placeholder="Please input password"
                show-password
            />
        </div>
        <div class="button_login">
            <el-button type="primary">登陆</el-button>
        </div>
    </div>
</template>

<script setup>
import {ref} from 'vue'
import Header from '../components/Header.vue'
const inputusername = ref('')
const inputpassword = ref('')

</script>

<style>
.input{
    display: flex;
    flex-direction: column;
    justify-content: center; 
    align-items: center;
    margin-top: 100px;
}
.input_row{
    display: flex;
    align-items:center;
    margin-bottom:20px; 
}
.input_u, .input_p{
    margin-left: 10px;
}
.button_login{
    margin-left: 50px;
}
</style>