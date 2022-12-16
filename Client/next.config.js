/** @type {import('next').NextConfig} */

const nextConfig = {
  reactStrictMode: true,
  basePath: '/sign-language',
  assetPrefix: '/sign-language',
  webpack: (config) => {
    const cvConfig = {
      fallback: {
        fs: false,
        path: false,
        crypto: false,
      },
    };
    config = { ...config, resolve: { ...config.resolve, ...cvConfig } };
    return config;
  },
};

module.exports = nextConfig;
