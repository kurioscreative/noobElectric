var webpack = require('webpack');
module.exports = {
  entry: [
    "./js/index.jsx"
  ],
  output: {
    path: __dirname + '/static',
    filename: "bundle.js"
  },
  module: {
    loaders: [
      {
        test: /\.js?$/,
        loader: 'babel-loader',
        query: {
          presets: ['es2015', 'react']
        },
        exclude: /node_modules/
    },
    {
        test: /\.jsx$/,
        loader: 'babel-loader',
        query: {
          presets: ['es2015', 'react']
        },
        exclude: /node_modules/
    },
    {
        test: /\.less$/,
        loader: "style!css!less"
    }
    ]
  },
  resolve: {
    extensions: ['', '.js', '.jsx']
},
  plugins: [
  ]
};
