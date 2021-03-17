module.exports = {
  webpack: (config, { isServer }) => {
    // Fixes npm packages that depend on `fs` module
    // without this we get
    // ./node_modules/@babel/core/lib/transformation/normalize-file.js:9:0
    // Module not found: Can't resolve 'fs'
    // null
    // as a result of next-mdx-remote
    // ref: https://coderberry.com/posts/mdx_next
    if (!isServer) {
      config.node = {
        fs: "empty",
      };
    }

    return config;
  },
};
