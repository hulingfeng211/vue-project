<template>
    <div id="app">

        <nav-bar></nav-bar>
        <div style="">
        <el-row >
            <el-col :span="4">
                <side-bar></side-bar>
            </el-col>
            <el-col :span="16">
               <router-view></router-view>
            </el-col>
        </el-row>
         </div>
         <!--
        <footer2></footer2> -->
        


    </div>
</template>

<script>
import SideBar from './components/SideBar'
import Footer2 from './components/Footer2'
import NavBar from './components/NavBar'
import Markdown from './components/Markdown'

export default {
  data () {
    return {
      msg: 'Use Vue 2.0 Today!'
    }
  },
  methods: {

     handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
  },
   components:{

            SideBar,Footer2,NavBar,Markdown
        }
}


</script>

<style>




</style>
