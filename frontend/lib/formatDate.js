
export function formatDate(date) {
    const date_input = new Date(date);
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    const date_fmt = date_input.toLocaleDateString(undefined, options);
    return date_fmt
  }
  