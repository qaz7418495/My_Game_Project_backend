<template>
    <div class="common-layout">
        <div class="Header">
            <Header/>
        </div>
        <div class="Lunbotu">
            <Lunbotu/>
        </div>
        <div class="Main">
            <div class="Video">
                <div class="Video-title">Ekat残局1v4冷静面对，枪法与意识并存，拿下残局！</div>
                <video class="Video-mp4" src="../assets/video/ekat-1.mp4" controls></video>
                <div class="Video-title">开心果阿卡丽千里追击，怎奈防御塔技高一筹，遗憾落败！</div>
                <video class="Video-mp4" src="../assets/video/lhy-1.mp4" controls></video>
            </div>
        </div>
        <div class="Bottom">
            <p>VX：leeball1014</p>
            <p>Email：466034604@qq.com</p>
            <p>All Rights Reserved. leeball 版权所有</p>
        </div>
    </div>
</template>
  
<script setup>
import Header from '../components/Header.vue';
import Lunbotu from '../components/Lunbotu.vue';
</script>

<style>
.Video{
    padding: 40px;
}
.Video-mp4{
    padding: 20px;
    width: 600px;
}
.Main{
    text-align: center;
    margin-top: 40px;
    background-color: rgb(233, 233, 233);
    border-radius: 5px;
}
.Bottom{
    padding: 2rem;
    text-align: center;
    background-color: whitesmoke;
    color: gray;
    font-size: small;
}

.Lunbotu{
    margin-top: 40px;
    padding-top: 40px;
    padding-bottom: 40px;
    background-color: rgb(239, 252, 252);
    border-radius: 5px;
}
</style>