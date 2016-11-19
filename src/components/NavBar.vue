<template>
    <div >
        <el-menu router="true"  theme="dark" default-active="1"  mode="horizontal" @select="handleSelect">
            <el-menu-item   index="3"><strong>XXX管理系统</strong></el-menu-item>
            <el-submenu style="float:right;" index="2">
                <template slot="title">我的工作台</template>
                <el-menu-item index="2-1">个人设置</el-menu-item>
                <el-menu-item index="2-2">系统设置</el-menu-item>
                <el-menu-item index="2-3">注销</el-menu-item>
            </el-submenu>
            <el-menu-item  style="float:right;" index="/list">订单管理</el-menu-item>
            <el-menu-item  style="float:right;" index="/">Home</el-menu-item>
            <el-menu-item  style="float:right;" index="/list">List</el-menu-item>
            <el-menu-item  style="float:right;" index="/notFound">Other</el-menu-item>
        </el-menu>
    </div>
</template>
<style>

</style>
<script>
    export default{
        data(){
            return{
            }
        },
        components:{
        },
        methods: {

            handleSelect(key, keyPath) {
                console.log(key, keyPath);
            }
         },
    }
</script>
