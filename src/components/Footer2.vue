<template>
    <div id="footer">
        <el-row >
            <el-col :span="24">
                <h4 style="align:center;">{{copyright}}</h4>
            </el-col>
        </el-row>
    </div>
</template>
<style>
  #footer {
    position: fixed;
    bottom: 0;
    text-align: center;
    background-color:#E5E9F2;
    width: 100%;
}
</style>
<script>
    export default{
        name:"Footer2",
        data(){
            return{
                copyright:"2016-China SWS"
            }
        },
        components:{
        }
    }
</script>
