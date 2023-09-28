<template>
    <el-carousel :interval="4000" type="card" height="300px">
      <el-carousel-item 
      v-for="(image, index) in images" 
      :key="index"
      @click="navigate(image.link)">
        <img :src="image.src" alt="" style="width: 100%;height: 100%;">
      </el-carousel-item>
    </el-carousel>
  </template>
  
<script setup>
import {ref} from 'vue';
import csgo from '../assets/img/csgo.jpg';
import lol from '../assets/img/lol.jpg';
import valorant from '../assets/img/valorant.jpg';
import { useRouter } from 'vue-router';

const images = ref([
  {src:csgo, link:'/csgo'},
  {src:lol, link:'/lol'},
  {src:valorant, link:'/valorant'}
]);

let router=useRouter();

function navigate(link){
  router.push(link);
}
defineExpose({
  navigate
})
</script>

<style scoped>
.el-carousel__item h3 {
color: #475669;
opacity: 0.75;
line-height: 300px;
margin: 0;
text-align: center;
}

.el-carousel__item:nth-child(2n) {
background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
background-color: #d3dce6;
}
</style>
