module.exports = {
  env: {
    BACKEND_URI: 'http://backend:8000'
  },
  webpack: (config, { isServer }) => {

    if (!isServer) {
      // don't resolve 'fs' module on the client to prevent this error on build --> Error: Can't resolve 'fs'
      config.resolve.fallback = {
        // fs: false
        fs: false,
        path: false,
        child_process: false, 
        crypto: false,
        os: false,
        tty: false
      }
    }

    return config;
  }
};
