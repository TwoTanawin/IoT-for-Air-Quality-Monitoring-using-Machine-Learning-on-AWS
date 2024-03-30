<template>
    <li>
        <img src="https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg"/>
        <hr>
        <slot></slot>
    </li>
</template>

<script>
export default {

}

</script>

<style scoped>
li {
    margin: 1rem 0;
    font-size: 1.25rem;
    font-weight: bold;
    background: purple;
    padding: 0.5rem;
    border-radius: 25px;
    color: white;
}
img{
    width: 100px;
    height: 100px;
}

/* button{
    font: inherit;
    cursor: pointer;
    border: 1px solid #ff0077;
    background: #ff0077;
    color: white;
    padding: 0.05rem 1rem;
    box-shadow: 1px 2px rgba(0, 0, 0, 0.26);
}
.fade-enter-from{
    opacity: 0;
}
.fade-enter-active{
    transition: all 0.5s linear;
} */
</style>