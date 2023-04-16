// 导入 axios
import axios from 'axios'

// 创建 axios 实例
const API =axios.create({
    // 设置请求头
    headers:{
        'Content-Type':'application/json'
    },
    // 设置请求地址
    baseURL:'http://127.0.0.1:5008/api/',
    // 设置超时时间
    timeout: 2000
})
export default API