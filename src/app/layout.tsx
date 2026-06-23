import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'VED CHAUHAN — Full Stack Developer',
  description:
    'Production-ready systems, scalable applications, modern architectures. Portfolio of VED CHAUHAN.',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
