<template>
    <div id="side-bar">
    <el-row class="tac">
        <el-col :span="24">
            <el-menu router="true" default-active="2" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose">
                <el-submenu index="1">
                    <template slot="title"><i class="el-icon-message"></i>Container Manager</template>
                    <el-menu-item-group title="分组一">
                        <el-menu-item index="1-1">Container</el-menu-item>
                        <el-menu-item index="1-2">Add Container</el-menu-item>
                    </el-menu-item-group>
                    <el-menu-item-group title="分组2">
                        <el-menu-item index="1-3">选项3</el-menu-item>
                    </el-menu-item-group>
                </el-submenu>
                <el-submenu index="1">
                    <template slot="title"><i class="el-icon-message"></i>Vue Examples </template>
                     
                        <el-menu-item index="/markdown">MarkDown</el-menu-item>
                        <el-menu-item index="1-2">Add Container</el-menu-item>
                    
                    <el-menu-item-group title="分组2">
                        <el-menu-item index="1-3">选项3</el-menu-item>
                    </el-menu-item-group>
                </el-submenu>
                <el-menu-item index="2"><i class="el-icon-menu"></i>导航二</el-menu-item>
                <el-menu-item index="3"><i class="el-icon-setting"></i>导航三</el-menu-item>
            </el-menu>
        </el-col>

    </el-row>
    </div>

</template>
<style>
    #side-bar{
        min-height: 768px;
     }

</style>
<script>
  export default {
    name:"SideBar",
    methods: {
      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }

</script>

