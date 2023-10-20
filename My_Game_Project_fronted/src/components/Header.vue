<template>
  <div class="Top">
    <a href="http://www.baidu.com" target="_blank"><img class="Icon" src="../assets/img/icon.jpg" alt="找不到图片"></a>
    <router-link :to="{ name: 'Main'}" class="Title" title="欢迎来到lb的Game Project！">b1mple's Game Project</router-link>
    <avator class="Avator"/>
    <router-link :to="{ name: 'Welcome'}" class="button-lr" style="margin-left: 30px;">
      <el-button type="primary">登陆</el-button>
    </router-link>
  </div>
  <div class="h-6" />
  <el-menu
    :default-active="activeIndex"
    class="el-menu-demo"
    mode="horizontal"
    background-color="#545c64"
    text-color="#fff"
    active-text-color="#ffd04b"
    @select="handleSelect"
  >
    <router-link :to="{ name: 'Main'}">
      <el-menu-item index="1">Game Center</el-menu-item>
    </router-link>
    <el-sub-menu index="2">
      <template #title>GAMES</template>
      <router-link :to="{ name: 'Csgo'}">
        <el-menu-item index="2-1">CSGO</el-menu-item>
      </router-link>
      <router-link :to="{ name: 'Lol'}">
        <el-menu-item index="2-2">League of Legends</el-menu-item>
      </router-link>
      <router-link :to="{ name: 'Valorant'}">
        <el-menu-item index="2-3">Valorant</el-menu-item>
      </router-link>
    </el-sub-menu>
    <el-menu-item index="3" disabled>Info</el-menu-item>
    <el-menu-item index="4">Orders</el-menu-item>
  </el-menu>
</template>
  
<script lang="ts" setup>
import { ref } from 'vue'
import avator from './Avator.vue'
const activeIndex = ref('1')
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
</script>

<style scoped>
.Avator{
  margin-left: auto;
  padding-top: 25px;
}
.button-lr{
  margin-left: auto;
}
.Title{
    color: rgb(127, 193, 255);  
    font-size: 30px;
    float: left;
    margin-left: 50px;
    font-weight: bold;
}
.Top{
    line-height: 100px;
    height: 100px;
    display: flex;
    justify-content: center;
    align-items: center ;
}
.Bottom{
   padding: 2rem;
   text-align: center;
   background-color: whitesmoke;
   color: gray;
   font-size: small;
}
.Icon{
    width: 50px;
    height: 50px;
    float: left;
}
</style>