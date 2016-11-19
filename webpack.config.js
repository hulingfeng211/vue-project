var webpack = require("webpack");
var path = require('path');

module.exports = {
    entry: {
        bundle: ["./src/main.js"]
    },
    output: {
        path: __dirname,
        publicPath: "/",
        filename: "dist/[name].js"
    },
    module: {
        loaders: [
            {test: /\.html$/, loaders: ['html']},
            {test: /\.vue$/, loaders: ['vue']},
            {
                test: /\.css$/,
                loader: 'style-loader!css-loader'
            },
            {
                test: /(\.js)$/, loader: ["babel"], exclude: /node_modules/,
                query: {
                    presets: ["es2015"]
                }
            },
            {
                test: /\.(eot|ttf|woff|png|jpe?g|gif|svg)(\?\S*)?$/,
                loader: 'file-loader',
                query: {
                    name: './static/[name].[ext]?[hash]'
                }
            }
        ]
    },
    resolve: {
        extensions: ['', '.js', '.vue'],
        alias: {
            vue: 'vue/dist/vue.js',
            filter: path.join(__dirname, './src/filters'),
            components: path.join(__dirname, './src/components')
        }
    },
    babel: {
        presets: ['es2015'],
        plugins: ['transform-runtime']
    },
    plugins: [
        /*
         new webpack.optimize.UglifyJsPlugin({
         compress: {
         warnings: false
         }
         })
         */
    ]
};