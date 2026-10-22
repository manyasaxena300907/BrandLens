// frontend/app/layout.js
// Shared page frame: the navbar and global styles wrap every page.
// TODO: add <Navbar /> and global styles.

export const metadata = { title: "BrandLens" };

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
