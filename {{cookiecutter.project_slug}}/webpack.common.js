var MiniCssExtractPlugin = require('mini-css-extract-plugin')
var CopyWebpackPlugin = require('copy-webpack-plugin')
var webpack = require('webpack')
var path = require('path')
var autoprefixer = require('autoprefixer')

module.exports = {
  entry: {
    adhocracy4: [
      './{{ cookiecutter.project_slug}}/assets/scss/style.scss',
      './{{ cookiecutter.project_slug}}/assets/js/app.js'
    ],
    vendor: [
      'classnames',
      '@fortawesome/fontawesome-free/scss/fontawesome.scss',
      '@fortawesome/fontawesome-free/scss/brands.scss',
      '@fortawesome/fontawesome-free/scss/regular.scss',
      '@fortawesome/fontawesome-free/scss/solid.scss',
      'jquery',
      'js-cookie',
      'react',
      'immutability-helper',
      'react-dom',
      'react-flip-move',
    ],
{% if cookiecutter.add_maps_and_mapideas_app == 'y' %}
    leaflet: [
      'leaflet',
      'leaflet/dist/leaflet.css',
      'leaflet-draw',
      'leaflet-draw/dist/leaflet.draw.css',
      'leaflet.markercluster',
      'leaflet.markercluster/dist/MarkerCluster.css',
    ],
    'leaflet.draw': [
      'leaflet-draw',
      'leaflet-draw/dist/leaflet.draw.css'
    ],
{% endif %}
    datepicker: [
      './{{ cookiecutter.project_slug}}/assets/js/init-picker.js',
      'datepicker/css/datepicker.min.css'
    ]
  },
  output: {
    libraryTarget: 'this',
    library: '[name]',
    path: path.resolve('./{{ cookiecutter.project_slug}}/static/'),
    publicPath: '/static/',
    filename: '[name].js'
  },
  externals: {
    'django': 'django'
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules\/(?!adhocracy4|bootstrap)/, // exclude most dependencies
        loader: 'babel-loader',
        options: {
          presets: ['babel-preset-env', 'babel-preset-react'].map(require.resolve)
        }
      },
      {
        test: /\.s?css$/,
        use: [
          {
            loader: MiniCssExtractPlugin.loader
          },
          {
            loader: 'css-loader'
          },
          {
            loader: 'postcss-loader',
            options: {
              ident: 'postcss',
              plugins: (loader) => [
                autoprefixer()
              ]
            }
          },
          {
            loader: 'sass-loader'
          }
        ]
      },
      {
        test: /fonts\/.*\.(svg|woff2?|ttf|eot)(\?.*)?$/,
        loader: 'file-loader',
        options: {
          name: 'fonts/[name].[ext]'
        }
      },
      {
        test: /\.svg$|\.png$/,
        loader: 'file-loader',
        options: {
          name: 'images/[name].[ext]'
        }
      }
    ]
  },
  resolve: {
    extensions: ['*', '.js', '.jsx', '.scss', '.css'],
    alias: {
      'jquery$': 'jquery/dist/jquery.min.js',
      'shariff$': 'shariff/dist/shariff.complete.js'
    },
    // when using `npm link`, dependencies are resolved against the linked
    // folder by default. This may result in dependencies being included twice.
    // Setting `resolve.root` forces webpack to resolve all dependencies
    // against the local directory.
    modules: [path.resolve('./node_modules')]
  },
  plugins: [
    new webpack.ProvidePlugin({
      timeago: 'timeago.js'
    }),
    new webpack.optimize.SplitChunksPlugin({
      name: 'vendor',
      filename: 'vendor.js'
    }),
    new MiniCssExtractPlugin({
      filename: '[name].css',
      chunkFilename: '[id].css'
    }),
    new CopyWebpackPlugin([
      {
        from: './{{ cookiecutter.project_slug}}/assets/images/**/*',
        to: 'images/',
        flatten: true
      }
    ])
  ]
}
