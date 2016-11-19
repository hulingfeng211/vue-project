<template>
    <div>
        <div>this is List</div>
        <div>this is List</div>
        <div>this is List</div>
        <div>this is List</div>
        <div>this is List</div>
        <div>this is List</div>
        <div>this is List</div>
        <div>this is List</div>
        <div>this is List</div>
        <div>this is List</div>
        <h1>{{msg|capitalize}}</h1>
        <h2>{{fullName}}</h2>
        <div class="red_bg">
        <input v-model="firstName">
        <input v-model="lastName">
            </div>
    </div>
</template>
<style>
    .red_bg {
            background-color:red;
    }


</style>
<script>
    export default{
      data(){
        return{
                msg:'hello vue',
                    firstName: 'Foo',
                    lastName: 'Bar',
                    fullName: 'Foo Bar'
            }
        },
          filters: {
            capitalize: function (value) {
                if (!value) return ''
                    value = value.toString()
                    return value.charAt(0).toUpperCase() + value.slice(1)
                }
        },
        watch:{
            firstName:function(val){
                this.fullName=val+' '+this.lastName;
            },
            lastName:function(val){
                this.fullName=this.firstName+' '+val;
            }
        },
        components:{
        }
    }


</script>
