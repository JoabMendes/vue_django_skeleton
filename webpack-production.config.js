const path = require('path');
const webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var Dotenv = require('dotenv-webpack');
const { VueLoaderPlugin } = require('vue-loader');
var WriteFilePlugin  = require('write-file-webpack-plugin');

module.exports = {
    entry: './src/main.js',
    output: {
        path: path.resolve(__dirname, './static'),
        publicPath: '/static/',
        filename: 'build.js'
    },
    plugins: [
        new BundleTracker({filename: 'webpack-production-stats.json'}),
        new WriteFilePlugin(),
        new Dotenv({
            systemvars: true
        }),
        new VueLoaderPlugin(),
        new webpack.DefinePlugin({
            'process.env': {
                NODE_ENV: '"production"'
            }
        }),
        new webpack.LoaderOptionsPlugin({
            minimize: true,
            options: {
               productionSourceMap: false
            }
        })
    ],
    module: {
        rules: [
            {
                test: /\.css$/,
                use: [
                    'vue-style-loader',
                    'css-loader'
                ],
            },
            {
                test: /\.scss$/,
                use: [
                    'vue-style-loader',
                    'css-loader',
                    'sass-loader'
                ],
            },
            {
                test: /\.sass$/,
                use: [
                    'vue-style-loader',
                    'css-loader',
                    'sass-loader?indentedSyntax'
                ],
            },
            {
                test: /\.vue$/,
                loader: 'vue-loader',
                options: {
                    loaders: {
                        // Since sass-loader (weirdly) has SCSS as its default parse mode, we map
                        // the "scss" and "sass" values for the lang attribute to the right configs here.
                        // other preprocessors should work out of the box, no loader config like this necessary.
                        'scss': [
                            'vue-style-loader',
                            'css-loader',
                            'sass-loader'
                        ],
                        'sass': [
                            'vue-style-loader',
                            'css-loader',
                            'sass-loader?indentedSyntax'
                        ]
                    }
                    // other vue-loader options go here
                }
            },
            {
                test: /\.js$/,
                loader: 'babel-loader',
                exclude: /node_modules/
            },
            {
                test: /\.(png|jpg|gif|svg)$/,
                loader: 'file-loader',
                options: {
                    name: '[name].[ext]?[hash]'
                }
            }
        ]
    },
    resolve: {
        alias: {
            'vue$': 'vue/dist/vue.esm.js'
        },
        extensions: ['*', '.js', '.vue', '.json']
    },
    devServer: {
        historyApiFallback: true,
        client: {
            overlay: true,
        }
    },
    performance: {
        hints: false
    },
    devtool: 'source-map',
    optimization: {
        minimize: true,
        minimizer: [
            new TerserPlugin({
                sourceMap: false,
                extractComments: true,
                terserOptions: {
                    warnings: false
                }
            })
        ],
    }
}
